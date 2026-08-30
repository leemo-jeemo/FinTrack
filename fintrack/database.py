import sqlite3
import pathlib

DATABASE_PATH = pathlib.Path("data/fintrack.db")


def get_connection():
    return sqlite3.connect(DATABASE_PATH)


def initialize_database():
    connection = get_connection()
    connection.execute(
        """CREATE TABLE IF NOT EXISTS transactions(id INTEGER PRIMARY KEY, date TEXT, amount REAL, type TEXT, category TEXT, description TEXT)"""
    )
    connection.commit()
    connection.close()

