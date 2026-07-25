from flask import Blueprint, render_template, request, redirect, session
from werkzeug.security import check_password_hash
import sqlite3

auth = Blueprint("auth", __name__)
DB_PATH = "database/db.sqlite3"


def get_db_connection():
    return sqlite3.connect(DB_PATH)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()
        conn.close()

        # user columns: (id, username, password_hash, role)
        if user and check_password_hash(user[2], password):
            session["user_id"] = user[0]
            session["role"] = user[3]
            return redirect("/dashboard")
        return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")


@auth.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
