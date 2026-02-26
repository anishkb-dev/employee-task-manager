import sqlite3

DB_PATH = "database/db.sqlite3"


def get_db_connection():
    return sqlite3.connect(DB_PATH, timeout=10)


def create_tasks_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            status TEXT NOT NULL,
            assigned_to INTEGER,
            FOREIGN KEY (assigned_to) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()


def create_task(title, user_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, status, assigned_to) VALUES (?, ?, ?)",
        (title, "todo", user_id)
    )

    conn.commit()
    conn.close()


def get_tasks_for_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, title, status FROM tasks WHERE assigned_to=?",
        (user_id,)
    )

    tasks = cursor.fetchall()
    conn.close()
    return tasks


def update_task_status(task_id, status):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET status=? WHERE id=?",
        (status, task_id)
    )

    conn.commit()
    conn.close()


def get_tasks_for_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, status, assigned_to FROM tasks")
    all_tasks = cursor.fetchall()
    print("ALL TASKS IN DB =", all_tasks)

    cursor.execute(
        "SELECT id, title, status FROM tasks WHERE assigned_to=?",
        (user_id,)
    )
    tasks = cursor.fetchall()

    conn.close()
    return tasks
