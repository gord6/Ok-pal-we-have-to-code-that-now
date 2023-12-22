#!/bin/bash


python /core/db_setup/init_db.py
cd /core
flask --debug run --host 0.0.0.0 