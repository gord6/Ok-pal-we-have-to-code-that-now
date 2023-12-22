#!/bin/bash


python /app/db_setup/init_db.py

SCRIPT_NAME=/student-survey gunicorn --config gunicorn_config.py wsgi:app
