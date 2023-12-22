from modules._db import _fetch


def select_actions():
    query = "SELECT * FROM actions;"
    results = _fetch(query)
    return results


def insert_actions(user_id, task_name, timestamp, action):
    query = (
        "INSERT INTO actions (user_id, task_name, timestamp, action) VALUES ('%s', '%s', %s, '%s') RETURNING ID"
        % (user_id, task_name, timestamp, action)
    )
    submission_id = _fetch(query, True)
    return submission_id
