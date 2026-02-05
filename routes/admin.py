from flask import Blueprint, render_template, request, redirect, session
from models.user import create_employee

admin = Blueprint("admin", __name__)



@admin.route("/admin", methods=["GET", "POST"])
def admin_dashboard():
    if session.get("role") != "admin":
        return redirect("/login")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        create_employee(username, password)

    return render_template("admin_dashboard.html")
