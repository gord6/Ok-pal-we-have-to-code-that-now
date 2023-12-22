import logging
import modules._db.tasks as db_tasks


def get_all_tasks():

    tasks = [{"name": t[0], "description": t[1], "order":t[2], "enabled":t[3], "chatgpt": t[4]}
             for t in db_tasks.get_all_tasks()]

    return sorted(tasks, key=lambda d: d['name'])


def update_tasks(tasks):
    for task in tasks:
        db_tasks.update_task(
            task["name"], task["enabled"], task["order"], task["chatgpt"], task["description"])


def insert_task(task):
    db_tasks.insert_task(
        task["name"], task["enabled"], task["order"], task["chatgpt"], task["description"])



def all_task_data():
    return db_tasks.full_table(), ["name", "description", "n_order", "enabled", "chatgpt"]


