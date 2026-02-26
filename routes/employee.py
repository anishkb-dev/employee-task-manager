from flask import Blueprint, render_template, session, redirect, request
from models.task import get_tasks_for_user, update_task_status

employee = Blueprint("employee", __name__)

@employee.route("/employee", methods=["GET", "POST"])
def employee_dashboard():
    if session.get("role") != "employee":
        return redirect("/login")

    user_id = session.get("user_id")
    print("SESSION USER_ID =", session.get("user_id"))

    if request.method == "POST":
        task_id = request.form["task_id"]
        status = request.form["status"]
        update_task_status(task_id, status)

    tasks = get_tasks_for_user(user_id)
    return render_template("employee_dashboard.html", tasks=tasks)


