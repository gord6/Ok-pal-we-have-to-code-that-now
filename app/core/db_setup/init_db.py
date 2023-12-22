import json
import psycopg2
import pathlib

import os

FILEPATH = pathlib.Path(__file__).parent.resolve()


PG_PW = os.environ.get("POSTGRES_PASSWORD")
PG_USER = os.environ.get("POSTGRES_USER")
PG_DB = os.environ.get("POSTGRES_DB")
PG_HOST = os.environ.get("POSTGRES_HOST")
PG_PORT = os.environ.get("POSTGRES_PORT")

STAGE = os.environ.get("STAGE")

if STAGE == "prod":
    print("Load production initialization... ")
    with open(str(FILEPATH) + "/db_setup_prod.json", "r") as f:
        db_setup = json.load(f)
else:
    with open(str(FILEPATH) + "/db_setup_dev.json", "r") as f:
        db_setup = json.load(f)


conn = psycopg2.connect(
    database=PG_DB, user=PG_USER, password=PG_PW, port=PG_PORT, host=PG_HOST
)
cursor = conn.cursor()


if STAGE != "prod":
    to_delete = [
        "questionnaire",
        "prompts",
        "submissions",
        "actions",
        "users",
        "tasks",
        "exc_groups",
    ]

    for table in to_delete:
        cursor.execute(f"DROP TABLE IF EXISTS {table};")


for table in db_setup["tables"]:
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {table["name"]} {table["signature"]};')


for table, insertions in db_setup["data"].items():
    for insertion in insertions:
        columns = ", ".join(insertion.keys())
        vals = ", ".join([f"'{v}'" for v in insertion.values()])
        cursor.execute(
            f"INSERT INTO {table} ({columns}) VALUES({vals}) ON CONFLICT DO NOTHING"
        )


conn.commit()

conn.close()
