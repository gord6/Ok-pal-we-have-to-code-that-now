from datetime import datetime
import logging

import flask_login
from werkzeug.security import generate_password_hash, check_password_hash
import modules._db.users as db_users
import modules._db.tasks as db_tasks
import modules._db.prompts as db_prompts
import modules._db.groups as db_groups


class User(flask_login.UserMixin):
    def __init__(self, name):
        self.id = name

    @classmethod
    def get_by_id(cls, user_id):
        if db_users.id_exists(user_id):
            return cls(user_id)
        else:
            return None


def get_current_task():
    task = db_tasks.get_current_task(flask_login.current_user.id)
    if not task:
        return
    else:
        return task[:2]


def chatgpt_allowed():
    allowed = db_tasks.get_current_task(flask_login.current_user.id)[4]
    return True if allowed == 1 else False


def user_is_allowed():
    allowed = db_users.group_is_allowed(flask_login.current_user.id)

    return True if allowed[0] == 1 else False


def user_is_admin():
    if flask_login.current_user.id == "admin":
        return True
    return False


def valid_id(user_id):
    if user_id:
        return True
    return False


def user_exists(user_id):
    return db_users.user_exists(user_id)


def get_all_users():
    return db_users.select_all()


def user_gave_consent():
    user_id = flask_login.current_user.id
    consent = db_users.get_consent(user_id)
    return True if consent == 1 else False


def user_set_consent(consent):
    db_users.set_consent(flask_login.current_user.id)


def login(user_id, password):
    if not db_users.user_exists(user_id):
        return 0

    if check_password_hash(db_users.get_password_hash(user_id), password):
        flask_login.login_user(User(user_id))
        return 1

    return 0


def delete_consent():
    db_users.delete_consent_data()


def insert_user(user_data):
    db_users.insert_user(
        user_data["name"],
        generate_password_hash(user_data["pw"], "pbkdf2:sha256:1000000"),
        user_data["group"],
    )


def get_groups():
    return db_groups.get_all_groups()


def update_groups(groups):
    for group in groups:
        db_groups.update_group(group)


def update_group(username, group):
    db_users.update_group(username, group)


def all_user_data():
    return db_users.full_table(), ["id", "pw_hash", "current_task", "exc_group", "consent"]


def all_group_data():
    return db_groups.full_table(), ["name", "activated"]
