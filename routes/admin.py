from flask import Blueprint, render_template, request, redirect, session, url_for
from models.user import create_employee, get_all_employees
from models.task import create_task


admin = Blueprint("admin", __name__)


@admin.route("/admin", methods=["GET", "POST"])
def admin_dashboard():
    if session.get("role") != "admin":
        return redirect("/login")

    status = None

    if request.method == "POST":

     
        if "username" in request.form:
            username = request.form["username"]
            password = request.form["password"]

            success = create_employee(username, password)
            status = "employee_created" if success else "employee_exists"

     
        elif "title" in request.form:
            title = request.form["title"]
            user_id = int(request.form["user_id"])
            create_task(title, user_id)
            status = "task_created"

    employees = get_all_employees()

    return render_template(
        "admin_dashboard.html",
        status=status,
        employees=employees
    )


