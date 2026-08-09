# to do list project
a To-Do-List program
# To-Do List — Django Project

A full-featured to-do list web application built with Django as part of my journey learning backend development.

## Features

- User authentication (signup, login, logout)
- Each user only sees and manages their own tasks
- Create, edit, delete, and mark tasks as complete
- Task deadlines
- Custom categories per user
- Django Admin panel for management
- Basic responsive styling with custom CSS

## Tech Stack

- Python
- Django
- SQLite (default development database)
- HTML / CSS

## Project Structure

## Setup & Installation

1. Clone the repository
```bash
   git clone <your-repo-url>
   cd "to do list project"
```

2. Create and activate a virtual environment
```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
```

3. Install dependencies
```bash
   pip install django
```

4. Run migrations
```bash
   python manage.py migrate
```

5. Create a superuser (optional, for admin access)
```bash
   python manage.py createsuperuser
```

6. Run the development server
```bash
   python manage.py runserver
```

7. Visit `http://127.0.0.1:8000/` in your browser

## What I Learned

This project was built step by step while learning Django fundamentals: models, migrations, views, templates, forms, URL routing, static files, authentication, and access control.

## Status

This is a learning project, still evolving as I continue studying backend development.
