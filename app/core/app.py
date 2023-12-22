import os
import json
import logging
import time
from datetime import datetime

import flask
import flask_login
import pandas as pd


from modules import users, data, chatbot, access
import modules.tasks

from werkzeug.middleware.proxy_fix import ProxyFix

app = flask.Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY")
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


PROXY_PATH_PREFIX = os.environ.get("PROXY_PATH_PREFIX")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DUMMY_MESSAGE = msg = """Currently no OpenAI key provided. This is an example message to show how messages are displayed. Please provide an API key in your .env if you want to try the application with GPT3.5-turbo. <FINISH>"""


if PROXY_PATH_PREFIX:
    app.wsgi_app = ProxyFix(app.wsgi_app)


@login_manager.user_loader
def user_loader(user_id):
    return users.User.get_by_id(user_id)


@login_manager.unauthorized_handler
def unauthorized_handler():
    return flask.redirect(flask.url_for("login", next=flask.request.endpoint))


@app.route("/")
def index():
    return flask.redirect(flask.url_for("start"))


def redirect_dest(fallback):
    destination = flask.request.args.get("next")
    try:
        destination = flask.url_for(destination)
    except:
        return flask.redirect(fallback)
    return flask.redirect(destination)


@app.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "GET":
        return flask.render_template("login.html")

    user_id = flask.request.form["name"]
    password = flask.request.form["pw"]
    login_success = users.login(user_id, password)

    return (
        redirect_dest(fallback=flask.url_for("start")) if login_success else "Bad Login"
    )


@app.route("/logout")
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return flask.redirect(flask.url_for("login"))


@app.route("/start", methods=["POST", "GET"])
@flask_login.login_required
@access.time_constrained
@access.task_constrained
@access.data_privacy_regulation_signed
def start():
    if flask.request.method == "GET":
        task_nr, task = users.get_current_task()
        return flask.render_template(
            "start.html", task_nr=task_nr, task=task, path_prefix=PROXY_PATH_PREFIX
        )

    return flask.redirect(flask.url_for("chat"))


@app.route("/chat", methods=["GET", "POST"])
@flask_login.login_required
@access.time_constrained
@access.task_constrained
@access.data_privacy_regulation_signed
def chat():
    if not users.chatgpt_allowed():
        return flask.redirect(flask.url_for("submit"))

    if flask.request.method == "GET":
        task_nr, task = users.get_current_task()
        return flask.render_template(
            "chat.html", task_nr=task_nr, task=task, path_prefix=PROXY_PATH_PREFIX
        )


@app.route("/get_bot_response", methods=["POST"])
@flask_login.login_required
@access.time_constrained
@access.task_constrained
@access.data_privacy_regulation_signed
def get_bot_response():
    prompt = flask.request.data.decode("utf-8")
    messages = chatbot.generate_messages(prompt)

    def stream_response():
        if OPENAI_API_KEY=="None":            
            for event in DUMMY_MESSAGE.split(" "):
                time.sleep(0.05)
                if event == '<FINISH>':
                    yield "data: <FINISH>\n\n"
                yield "data: %s\n\n" % (
                        "<start>" + event + " <end>"
                    )
        else:
            try:
                for line in chatbot.get_response(messages):
                    if line.choices[0]["finish_reason"]:
                        yield "data: <FINISH>\n\n"
                    token = (
                        str(line.choices[0]["delta"]["content"])
                        if "content" in line.choices[0]["delta"]
                        else ""
                    )
                    yield "data: %s\n\n" % (
                        "<start>" + token.replace("\n", "<br/>") + "<end>"
                    )
            except Exception as e:
                logging.error(e)
                yield "data: <ERROR>\n\n"

    return app.response_class(stream_response(), mimetype="text/event-stream")


@app.route("/test_stream", methods=["GET", "POST"])
@flask_login.login_required
@access.time_constrained
@access.task_constrained
@access.data_privacy_regulation_signed
def test_stream():
    logging.error()

    def stream():
        for i in range(100):
            yield "data: %s\n\n" % str(i)

    return app.response_class(stream(), mimetype="text/event-stream")


@app.route("/feedback", methods=["POST"])
@flask_login.login_required
@access.time_constrained
@access.task_constrained
@access.data_privacy_regulation_signed
def feedback():
    feedback = flask.request.form.get("feedback")
    prompt = flask.request.form.get("userInput")
    answer = flask.request.form.get("botMsg")

    data.collect_prompt_data(prompt, answer, feedback)
    return "Success", 200


@app.route("/action", methods=["POST"])
@flask_login.login_required
@access.time_constrained
@access.task_constrained
@access.data_privacy_regulation_signed
def action():
    action = flask.request.form.get("action")
    task = flask.request.form.get("task")

    data.log_action(action, task=task)
    return "Success", 200


@app.route("/privacy_consent", methods=["POST"])
@flask_login.login_required
@access.time_constrained
@access.task_constrained
def privacy_consent():
    consent = tuple(flask.request.form.to_dict().values())
    users.user_set_consent(consent)

    return flask.redirect(flask.url_for("start"))


@app.route("/submit", methods=["POST", "GET"])
@flask_login.login_required
@access.time_constrained
@access.task_constrained
@access.data_privacy_regulation_signed
def submit():
    if flask.request.method == "GET":
        task_nr, _ = users.get_current_task()
        return flask.render_template(
            "submit.html", task_nr=task_nr, path_prefix=PROXY_PATH_PREFIX
        )

    history_files = flask.request.files.getlist("history")
    solution_files = flask.request.files.getlist("solution")
    questionnaire_values = tuple(flask.request.form.to_dict().values())
    data.collect_submission(solution_files, history_files, *questionnaire_values)
    data.log_action(
        "submission",
        task=questionnaire_values[3],
    )

    return json.dumps({"success": True}), 200, {"ContentType": "application/json"}


@app.route("/admin", methods=["GET"])
@flask_login.login_required
@access.only_admin
def admin():
    return flask.render_template("admin.html", path_prefix=PROXY_PATH_PREFIX)


def _make_csv_response(csv, filename, col_names):
    df = pd.DataFrame(csv)
    if len(df):
        df.columns = col_names
    resp = flask.make_response(df.to_csv(index=False))
    resp.headers[
        "Content-Disposition"
    ] = f"attachment; filename={filename + '-' + str(datetime.now()).replace(' ', '-')}.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp


@app.route("/tasks", methods=["POST", "GET"])
@flask_login.login_required
@access.only_admin
def tasks():
    if flask.request.method == "GET":
        tsks = modules.tasks.get_all_tasks()
        return flask.jsonify(tsks)

    logging.error(flask.request.get_json())
    try:
        if "type" in flask.request.get_json():
            modules.tasks.insert_task(flask.request.get_json())
        else:
            modules.tasks.update_tasks(flask.request.get_json())
        return json.dumps({"success": True}), 200, {"ContentType": "application/json"}
    except:
        logging.error("Fail")
        return json.dumps({"success": False}), 500, {"ContentType": "application/json"}


@app.route("/users", methods=["GET"])
@flask_login.login_required
@access.only_admin
def get_users():
    users = modules.users.get_all_users()
    return flask.jsonify(sorted(users, key=lambda d: d[0]))


@app.route("/update_user", methods=["POST"])
@flask_login.login_required
@access.only_admin
def update_user():
    logging.error(flask.request.get_json())
    try:
        username = flask.request.get_json()["user"]
        group = flask.request.get_json()["group"]
        users.update_group(username, group)

        return json.dumps({"success": True}), 200, {"ContentType": "application/json"}

    except:
        return json.dumps({"success": False}), 500, {"ContentType": "application/json"}


@app.route("/add_user", methods=["POST"])
@flask_login.login_required
@access.only_admin
def add_user():
    logging.error(flask.request.get_json())
    logging.error(flask.request.get_json())

    modules.users.insert_user(flask.request.get_json())
    return json.dumps({"success": True}), 200, {"ContentType": "application/json"}

@app.route("/download_data", methods=["GET"])
@flask_login.login_required
@access.only_admin
def download_data():
    table = flask.request.args.get("table")

    download_table = {
        "prompts": data.download_prompt_data,
        "questionnaire": data.download_questionnaire_data,
        "submissions": data.download_submission_data,
        "users": users.all_user_data,
        "tasks": modules.tasks.all_task_data,
        "exc_groups": users.all_group_data,
        "actions": data.download_action_data
    }
    
    content, col_names = download_table[table]()

    resp = _make_csv_response(content, table, col_names)
    return resp


@app.route("/groups", methods=["GET", "POST"])
@flask_login.login_required
@access.only_admin
def groups():
    if flask.request.method == "GET":
        groups = users.get_groups()
        return groups
    try:
        users.update_groups(flask.request.get_json())
        return json.dumps({"success": True}), 200, {"ContentType": "application/json"}
    except:
        return json.dumps({"success": False}), 500, {"ContentType": "application/json"}


@app.route("/delete_data", methods=["GET"])
@flask_login.login_required
@access.only_admin
def delete_data():
    return "Deleting data is not available", 500



if __name__ == "__main__":
    app.run(host="0.0.0.0")
