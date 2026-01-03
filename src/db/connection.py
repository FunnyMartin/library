# src/db/connection.py

import mysql.connector
from .config import load_config

def get_connection():
    cfg = load_config()
    return mysql.connector.connect(
        host=cfg["host"],
        port=cfg["port"],
        database=cfg["database"],
        user=cfg["user"],
        password=cfg["password"]
    )
