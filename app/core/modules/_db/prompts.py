import base64

from datetime import datetime, time
from modules._db import _fetch, _update


def encode(string_to_clean):
    tmp_bytes = string_to_clean.encode()
    return base64.b64encode(tmp_bytes).decode('ascii')


def decode(string_to_clean):
    tmp_bytes = string_to_clean.encode("ascii")
    return base64.b64decode(tmp_bytes).decode('ascii')


def insert_prompt(prompt, answer, feedback, user_id, task, timestamp):
    query = "INSERT INTO prompts (prompt, answer, feedback, user_id, task_name, timestamp) VALUES ('%s', '%s','%s', '%s', '%s', %s) RETURNING ID" % (
        prompt.replace("'", "''"), answer.replace("'", "''"), feedback, user_id, task, timestamp)
    prompt_id = _fetch(query, True)[0]
    return prompt_id


def insert_feedback(promptID, feedback, user_id, task):
    query = "UPDATE prompts SET feedback='%s' WHERE id=%s AND user_id='%s' AND task_name='%s';" % (
        feedback, promptID, user_id, task)
    _ = _update(query)


def load_prompt_history(user_id, task):
    query = "SELECT id, prompt, answer FROM prompts WHERE user_id='%s' AND task_name='%s';" % (
        user_id, task)
    result = _fetch(query)
    result = [(x[0], x[1].replace("''", "'"), x[2].replace("''", "'"))
              for x in result]
    return result


def select_prompts():
    query = "SELECT * FROM prompts;"
    return _fetch(query)
