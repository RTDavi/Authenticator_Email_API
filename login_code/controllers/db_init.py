import sqlite3


def db_init():
    with sqlite3.connect("logins") as db:
        db.cursor = db.cursor()
        db.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """)
        db.commit()