

from flask import Flask
from models.user import create_users_table
from models.task import create_tasks_table

app = Flask(__name__)
app.secret_key = "dev-secret-key"


def initialize_database():
    create_users_table()
    create_tasks_table()


@app.route("/")
def home():
    return "Employee Task Manager is running"


if __name__ == "__main__":
    initialize_database()  
    app.run(debug=True)
