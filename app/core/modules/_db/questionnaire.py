from modules._db import _fetch


def select_questionnaire():
    query = "SELECT * FROM questionnaire;"
    return _fetch(query)


def insert_questionnaire(task, user_id,  easier, confident, fun):
    query = "INSERT INTO questionnaire (task, user_id, feedback_easier, feedback_confident, feedback_fun) VALUES ('%s', '%s', %s, %s, %s) RETURNING ID" % (
        task, user_id,  easier, confident, fun)
    questionnaire_id = _fetch(query, True)
    return questionnaire_id
