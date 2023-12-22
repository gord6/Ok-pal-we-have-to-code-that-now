import logging

from datetime import datetime, time
from modules._db import _fetch, _update


def id_exists(user_id):
    result = _fetch("SELECT * FROM users WHERE id='%s'" % user_id, True)
    return True if result else False


def get_password_hash(user_id):
    result = _fetch("SELECT pw_hash FROM users WHERE id='%s'" % user_id, True)
    return result[0]


def user_exists(user_id):
    result = _fetch("SELECT * FROM users WHERE id='%s'" % user_id, True)
    if not result:
        return False
    return True


def group_is_allowed(user_id):
    query = (
        "SELECT activated FROM users JOIN exc_groups ON users.exc_group=exc_groups.name WHERE users.id='%s'"
        % user_id
    )
    return _fetch(query, True)


def get_consent(user_id):
    result = _fetch("SELECT consent FROM users WHERE id='%s'" % user_id, True)
    return result[0]


def set_consent(user_id):
    query = "UPDATE users SET consent=1 WHERE  id='%s';" % (user_id)
    _ = _update(query)


def delete_consent_data():
    query = "UPDATE users SET consent=0;"
    _ = _update(query)


def insert_user(name, pw, group):
    query = "INSERT INTO users(id, pw_hash, exc_group) VALUES ('%s', '%s', '%s')" % (
        name,
        pw,
        group,
    )
    _ = _update(query)


def select_all():
    result = _fetch("SELECT id, exc_group FROM users;")
    return result


def update_group(username, group):
    query = "UPDATE users SET exc_group='%s' WHERE  id='%s';" % (
        group, username)
    _ = _update(query)


def full_table():
    query = "SELECT * FROM users;"
    results = _fetch(query)
    return results

