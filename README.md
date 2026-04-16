# WhatBytes Assignment

Healthcare backend built with Django, Django REST Framework, JWT auth, and PostgreSQL-ready configuration.

## Tech Stack

- Django
- Django REST Framework
- djangorestframework-simplejwt
- PostgreSQL (via DATABASE_URL)
- drf-spectacular (Swagger and ReDoc)

## Prerequisites

- Python 3.11+ (project tested on newer versions as well)
- pip
- Optional: PostgreSQL running locally or hosted

## Setup

1. Copy `.env.example` to `.env` and set `SECRET_KEY` and `DATABASE_URL`.
2. Install dependencies with `pip install -r requirements.txt`.
3. Run migrations with `python manage.py makemigrations` and `python manage.py migrate`.
4. Start the server with `python manage.py runserver`.

## Environment Variables

- SECRET_KEY: Django secret key.
- DEBUG: True or False.
- ALLOWED_HOSTS: Comma-separated hosts, for example 127.0.0.1,localhost.
- DATABASE_URL: PostgreSQL URL. If omitted, project falls back to SQLite for local testing.
- JWT_ACCESS_LIFETIME: Access token lifetime in seconds.
- JWT_REFRESH_LIFETIME: Refresh token lifetime in seconds.

Example PostgreSQL URL format:

- postgresql://username:password@localhost:5432/database_name

## Run Options

- Windows quick start: start.bat
- Unix quick start: bash start.sh
- Manual run:
	- python manage.py migrate
	- python manage.py runserver

## API Documentation

- Swagger UI: http://localhost:8000/docs/
- ReDoc: http://localhost:8000/redoc/
- OpenAPI schema: http://localhost:8000/api/schema/

Use login endpoint first, then authorize in Swagger using Bearer token.

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

## Sample Request Bodies

Register:

{
	"name": "John Smith",
	"email": "john@example.com",
	"password": "SecurePass123"
}

Login:

{
	"email": "john@example.com",
	"password": "SecurePass123"
}

Create patient:

{
	"name": "Alice Johnson",
	"age": 35,
	"gender": "female",
	"address": "123 Main St",
	"medical_history": "Hypertension"
}

Create doctor:

{
	"name": "Dr. Michael Brown",
	"specialization": "Cardiology",
	"phone_number": "+1-555-0123",
	"email": "mbrown@hospital.com",
	"years_of_experience": 15
}

Create mapping:

{
	"patient_id": 1,
	"doctor_id": 1
}

## Testing

- Run Django tests:
	- python manage.py test
- You can also test all endpoints from Swagger UI.

## Expected Behavior

- Registration and login return user data and JWT tokens.
- Patient list and patient detail are scoped to the authenticated owner.
- Doctor endpoints are protected and require authentication.
- Mapping creation validates patient ownership and avoids duplicate patient-doctor assignments.

## Notes

- Patients are scoped to the authenticated user who created them.
- Doctor endpoints require authentication.
- Mapping creation validates patient ownership and prevents duplicates.

## Soft Delete Behavior

- Patient, doctor, and mapping delete endpoints use soft delete instead of hard delete.
- Deleted records are marked using `is_deleted=true` and `deleted_at=<timestamp>`.
- List and detail endpoints only return active records (`is_deleted=false`).
- Soft-deleted mapping records do not appear in mapping list responses.
- Soft-deleted patient-doctor mappings can be recreated for the same patient and doctor.