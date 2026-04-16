@echo off
REM Healthcare Backend Quick Start for Windows

setlocal enabledelayedexpansion

if not exist .env (
    echo Creating .env from example...
    copy .env.example .env
    echo. 
    echo .env created. Edit it to set your database and secret key.
)

echo Running migrations...
python manage.py migrate

echo.
echo Starting development server...
echo Server will run at http://localhost:8000
echo Admin panel at http://localhost:8000/admin/
python manage.py runserver
