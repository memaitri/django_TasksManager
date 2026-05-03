# Django Task Manager

A lightweight task management web app built with **Python** and **Django**.

## 🚀 What it does

- View tasks sorted by priority (highest first)
- Add tasks with a name and priority level (1–10)
- Toggle tasks as done/undone
- Delete tasks
- Session-based storage (tasks are stored per browser session)

## 🛠️ Tech Stack

- Python 3.13
- Django 6.0
- Django Templates (DTL)
- Session-based storage (SQLite-backed sessions)

## 📁 Project Structure

```
taskmanager/
├── manage.py
├── db.sqlite3
├── taskmanager/            # Project configuration
│   ├── settings.py
│   └── urls.py
└── tasks/                  # Tasks app
    ├── urls.py             # URL routing
    ├── views.py            # Business logic and form handling
    └── templates/tasks/
        ├── layout.html     # Base template
        ├── index.html      # Task list page
        └── add.html        # Add task form
```

## ⚙️ Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/memaitri/django_TasksManager.git
cd django_TasksManager

# Install Django
pip install django

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

### Usage

Open your browser and visit:

```
http://127.0.0.1:8000/tasks/
```

## 📌 Notes

- Tasks live in the Django session and reset when the browser session expires.
- No user authentication is required.
- The app uses no external CSS or JavaScript libraries.
