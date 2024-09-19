#!/bin/bash
echo "Collecting Static Files..."
python manage.py collectstatic --noinput
echo ====================================

echo "Creating Migrations..."
python manage.py makemigrations
echo ====================================

echo "Starting Migrations..."
python manage.py migrate
echo ====================================

echo "Starting Server..."
gunicorn rabbits_farm.wsgi:application --bind 0.0.0.0:8000