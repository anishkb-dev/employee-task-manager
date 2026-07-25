# Employee Task Manager 📋

> A role-based task management web app built with Flask and SQLite. Admins create employees and assign tasks; employees log in to view and update their own tasks.

**Tech:** Python · Flask · SQLite · Jinja2 · HTML/CSS

---

## Features

- 🔐 **Session-based authentication** with two roles — **admin** and **employee**
- 🛡️ **Role-guarded routes** — each dashboard redirects unauthorized users back to login
- 👥 **Admin** can create employee accounts and assign tasks to them
- ✅ **Employees** see only their own assigned tasks and update each task's status
- 🗄️ **Relational schema** — tasks reference users via a foreign key
- ⚙️ **Zero-config first run** — tables are created and a default admin is seeded automatically on startup
- 🚫 **Duplicate-user handling** — creating an existing username fails gracefully

---

## Architecture

The app uses Flask **blueprints** to separate concerns:

```
app.py                  # app factory, blueprint registration, DB bootstrap
├── routes/
│   ├── auth.py         # /login, /logout  — session login
│   ├── admin.py        # /admin           — create employees, assign tasks
│   └── employee.py     # /employee        — view & update assigned tasks
├── models/
│   ├── user.py         # users table, default admin, employee CRUD
│   └── task.py         # tasks table, task CRUD + status updates
├── templates/          # login, admin_dashboard, employee_dashboard (Jinja2)
└── database/db.sqlite3 # SQLite database (created on first run)
```

### Database schema

```
users                          tasks
-----                          -----
id        INTEGER PK           id           INTEGER PK
username  TEXT UNIQUE          title        TEXT
password  TEXT                 status       TEXT          (todo → in-progress → done)
role      TEXT                 assigned_to  INTEGER  ──FK──► users.id
```

---

## Routes

| Route | Method | Access | Purpose |
| ----- | ------ | ------ | ------- |
| `/login` | GET/POST | public | Authenticate and start a session |
| `/logout` | GET | any | Clear the session |
| `/dashboard` | GET | logged in | Redirects to the role-appropriate dashboard |
| `/admin` | GET/POST | admin | Create employees, assign tasks, list employees |
| `/employee` | GET/POST | employee | View assigned tasks, update task status |

---

## Run it locally

**Prerequisite:** Python ≥ 3.8

```bash
git clone https://github.com/anishkb-dev/employee-task-manager.git
cd employee-task-manager

python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

mkdir -p database                 # SQLite file lives here
python app.py
```

Open **http://127.0.0.1:5000/login**.

### Default admin login

On first run a default admin is created automatically:

| Username | Password |
| -------- | -------- |
| `admin`  | `admin123` |

Log in as admin → create an employee → assign them a task. Then log out and log in as that employee to update the task's status.

---

## Security

- **Passwords are hashed** with `werkzeug.security` (`generate_password_hash` /
  `check_password_hash`) — never stored in plaintext.
- The session-signing **`secret_key` comes from the `SECRET_KEY` env var** (with a
  dev-only fallback), and debug mode is off unless `FLASK_DEBUG=1`.
- All SQL uses parameterized `?` placeholders (no string interpolation → no SQL injection).

## Roadmap

- Add task due-dates, priorities, and a status dropdown UI
- Swap raw SQL for an ORM (SQLAlchemy) and add migrations
- Unit tests for the auth and task flows

---

> Built as a hands-on Flask project to practice role-based access, blueprints, and relational data modeling.
