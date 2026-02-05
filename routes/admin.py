from flask import Blueprint, render_template, session, redirect

admin = Blueprint("admin", __name__)


@admin.route("/admin")
def admin_dashboard():
    if session.get("role") != "admin":
        return redirect("/login")

    return render_template("admin_dashboard.html")
