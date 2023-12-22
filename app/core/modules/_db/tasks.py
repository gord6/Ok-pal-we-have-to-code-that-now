from datetime import datetime, time
from modules._db import _fetch, _update
import flask_login


def _get_enabled_tasks():
    tasks = _fetch("SELECT * FROM tasks WHERE enabled=1;")
    return sorted(tasks, key=lambda x: x[2])


def _get_unsolved_tasks(user_id):
    tasks = _get_enabled_tasks()
    solved = _fetch(
        "SELECT submissions.task FROM users JOIN submissions ON users.id = submissions.user_id WHERE users.id='%s'" % user_id)

    return [t for t in tasks if t[0] not in [s[0] for s in solved]]


def get_current_task(user_id):
    unsolved = _get_unsolved_tasks(user_id)
    if not len(unsolved):
        return

    return unsolved[0]


def get_all_tasks():
    tasks = _fetch("SELECT * FROM TASKS;")
    return tasks


def update_task(name, enabled, order, chatgpt, description):
    chatgpt = 1 if chatgpt == "enabled" else 0
    enabled = 1 if enabled == "enabled" else 0
    query = "UPDATE tasks SET enabled=%s, n_order=%s, chatgpt=%s, description='%s' WHERE name='%s';" % (
        enabled, order, chatgpt, description, name)
    _ = _update(query)


def insert_task(name, enabled, order, chatgpt, description):
    chatgpt = 1 if chatgpt == "enabled" else 0
    enabled = 1 if enabled == "enabled" else 0
    query = "INSERT INTO tasks(name, enabled, n_order, chatgpt, description) VALUES ('%s', %s, %s, %s, '%s');" % (
        name, enabled, order, chatgpt, description)
    _ = _update(query)



def full_table():
    query = "SELECT * FROM tasks;"
    results = _fetch(query)
    return results

