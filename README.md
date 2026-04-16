# WhatBytes Assignment

Healthcare backend built with Django, Django REST Framework, JWT auth, and PostgreSQL-ready configuration.

## Setup

1. Copy `.env.example` to `.env` and set `SECRET_KEY` and `DATABASE_URL`.
2. Install dependencies with `pip install -r requirements.txt`.
3. Run migrations with `python manage.py makemigrations` and `python manage.py migrate`.
4. Start the server with `python manage.py runserver`.

## API Endpoints

- `POST /api/auth/register/`
- `POST /api/auth/login/`
- `POST /api/patients/`
- `GET /api/patients/`
- `GET /api/patients/<id>/`
- `PUT /api/patients/<id>/`
- `DELETE /api/patients/<id>/`
- `POST /api/doctors/`
- `GET /api/doctors/`
- `GET /api/doctors/<id>/`
- `PUT /api/doctors/<id>/`
- `DELETE /api/doctors/<id>/`
- `POST /api/mappings/`
- `GET /api/mappings/`
- `GET /api/mappings/<patient_id>/`
- `DELETE /api/mappings/<id>/`

## Notes

- Patients are scoped to the authenticated user who created them.
- Doctor endpoints require authentication.
- Mapping creation validates patient ownership and prevents duplicates.