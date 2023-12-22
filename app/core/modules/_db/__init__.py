import logging
import os
from datetime import datetime, time

import psycopg2


PG_PW = os.environ.get("POSTGRES_PASSWORD")
PG_USER = os.environ.get("POSTGRES_USER")
PG_DB = os.environ.get("POSTGRES_DB")
PG_HOST = os.environ.get("POSTGRES_HOST")
PG_PORT = os.environ.get("POSTGRES_PORT")


def _get_db_connection():
    return psycopg2.connect(
        database=PG_DB, user=PG_USER, password=PG_PW, port=PG_PORT, host=PG_HOST
    )


def _fetch(query, fetchone=False):
    conn = _get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone() if fetchone else cursor.fetchall()
    conn.commit()
    conn.close()
    return result


def _update(query):
    conn = _get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()


def delete_table(table):
    logging.error(table)

    query = "TRUNCATE %s;" % table
    _update(query)
