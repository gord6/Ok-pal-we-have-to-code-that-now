from modules._db import _fetch


def select_submissions():
    query = "SELECT * FROM submissions;"
    results = _fetch(query)
    return results


def insert_submission(task, submission_type, user_id, code, filename):
    query = (
        "INSERT INTO submissions (task, submission_type, user_id, code, filename) VALUES ('%s', '%s', '%s', '%s', '%s') RETURNING ID"
        % (
            task,
            submission_type,
            user_id,
            code.replace("'", "''"),
            filename.replace("'", "''"),
        )
    )
    submission_id = _fetch(query, True)
    return submission_id
