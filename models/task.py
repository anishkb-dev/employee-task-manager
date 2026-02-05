import sqlite3

DB_PATH = "database/db.sqlite3"


def get_db_connection():
    return sqlite3.connect(DB_PATH)


def create_tasks_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL,
            assigned_to INTEGER,
            FOREIGN KEY (assigned_to) REFERENCES users (id)
        )
    """)

    conn.commit()
    conn.close()
