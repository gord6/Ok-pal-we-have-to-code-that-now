from functools import wraps
from flask import render_template

import modules.users as users


def time_constrained(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(users.user_is_admin())
        if users.user_is_allowed() or users.user_is_admin():
            return func(*args, **kwargs)
        else:
            return render_template(
                "restriction.html",
                title="Momentan nicht verfügbar.",
                description="Der Service steht nur zu den offiziellen Übungszeiten zur Verfügung.",
            )

    return wrapper


def task_constrained(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if users.get_current_task():
            return func(*args, **kwargs)
        else:
            return render_template(
                "restriction.html",
                title="Vielen Dank für die Teilnahme",
                description="Für diese Woche stehen keine weiteren Aufgaben zur Verfügung.",
            )

    return wrapper


def only_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if users.user_is_admin():
            return func(*args, **kwargs)
        else:
            return render_template(
                "restriction.html",
                title="Kein Zugriff",
                description="Dieser Account hat keine Berechtigung auf diese Ressource zuzugreifen.",
            )

    return wrapper


def data_privacy_regulation_signed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if users.user_gave_consent():
            return func(*args, **kwargs)
        else:
            return render_template("privacy.html")

    return wrapper
