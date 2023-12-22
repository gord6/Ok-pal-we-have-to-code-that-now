from modules._db import _fetch, _update


def get_all_groups():
    return _fetch("SELECT name, activated from exc_groups;")


def update_group(group):
    act = 1 if group["activated"] == "activated" else 0
    query = "UPDATE exc_groups SET activated=%s WHERE name='%s';" % (
        act, group["name"])
    _ = _update(query)


def full_table():
    query = "SELECT * FROM exc_groups;"
    results = _fetch(query)
    return results
