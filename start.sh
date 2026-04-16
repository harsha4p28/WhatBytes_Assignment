#!/bin/bash

# Healthcare Backend Quick Start

set -e

echo "Creating .env from example..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✓ .env created. Edit it to set your database and secret key."
fi

echo "Running migrations..."
python manage.py migrate

echo "Starting development server..."
echo "Server will run at http://localhost:8000"
echo "Admin panel at http://localhost:8000/admin/"
python manage.py runserver
