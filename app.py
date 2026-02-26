

from flask import Flask, redirect, session
from models.user import create_users_table, create_default_admin
from models.task import create_tasks_table
from routes.auth import auth
from routes.admin import admin
from routes.employee import employee

app = Flask(__name__)
app.secret_key = "dev-secret-key"

app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(employee)


def initialize_database():
    create_users_table()
    create_tasks_table()
    create_default_admin()


@app.route("/")
def home():
    return "Employee Task Manager is running"


@app.route("/dashboard")
def dashboard():
    if session.get("role") == "admin":
        return redirect("/admin")
    return redirect("/employee")


if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)
