# Project Django 1

This is my first project with Python-Django!


## Installation

Install my-project with npm

Python version: 3.11.6
Django Version: 5.0.6

if you want to know the version of python you are using, use this:
```bash
python --version
```

To install venv of python use:
```bash
python -m vernv venv
```

Later, activate venv, upgrade pip if necessary and install also django.
```bash
venv\scripts\activate
python.exe -m pip install --upgrade pip
pip install django
```

Then we start the prject with python:
```bash
django-admin startproject <nombre_del_proyecto> .
```

Initialize the server:
```bash
python manage.py runserver
```
To stop the server `Ctrl+C`

Apply the firsts migrations:
```bash
python manage.py migrate
```

Create the first superuser (admin):
```bash
python manage.py createsuperuser
```

Now, use `runserver` and go to `http://127.0.0.1:8000/admin/` and login.