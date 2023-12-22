import logging
import time
import flask_login


from modules._db import delete_table
from modules._db.questionnaire import insert_questionnaire, select_questionnaire
from modules._db.submissions import insert_submission, select_submissions
from modules._db.tasks import get_current_task
from modules._db.prompts import insert_prompt, insert_feedback, select_prompts
from modules._db.actions import insert_actions, select_actions


def _context_data():
    user_id = flask_login.current_user.id
    try:
        task = get_current_task(user_id)[0]
    except:
        task = None
    timestamp = int(time.time())
    return user_id, task, timestamp


def _file_to_dict(f):
    return {"content": f.read().decode("utf-8"), "filename": f.filename}


def _read_files(files):
    return [_file_to_dict(f) for f in files]


def collect_submission(solution_files, history_files, easier, confident, fun, task):
    user_id, _, _ = _context_data()

    solution_files = _read_files(solution_files)
    history_files = _read_files(history_files)

    for f in solution_files:
        code = f["content"]
        solution_id = insert_submission(task, "solution", user_id, code, f["filename"])

    for f in history_files:
        solution_id = insert_submission(task, "history", user_id, code, f["filename"])

    insert_questionnaire(task, user_id, easier, confident, fun)


def collect_prompt_data(prompt, answer, feedback):
    user_id, task, timestamp = _context_data()
    promptID = insert_prompt(prompt, answer, feedback, user_id, task, timestamp)


def download_prompt_data():
    return select_prompts(), [
        "id",
        "prompt",
        "answer",
        "feedback",
        "user_id",
        "task",
        "time",
    ]


def download_questionnaire_data():
    return select_questionnaire(), [
        "id",
        "task",
        "user_id",
        "feedback_easier",
        "feedback_confident",
        "feedback_fun",
    ]


def download_submission_data():
    return select_submissions(), [
        "id",
        "task",
        "submission_type",
        "code",
        "filename",
        "user_id",
    ]


def delete_all(table):
    delete_table(table)


def log_action(action, task=None):
    if not task:
        user_id, task, timestamp = _context_data()
    else:
        user_id, _, timestamp = _context_data()

    return insert_actions(user_id, task, timestamp, action)


def download_action_data():
    return select_actions(), ["id", "user_id", "task", "timestamp", "action"]
