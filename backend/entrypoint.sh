#!/bin/bash
set -e  # Exit on any error

# Wait for DB to be ready (simple loop)
until nc -z db 3306; do
  echo "Waiting for MySQL..."
  sleep 3
done

# Run migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Start Django dev server (for debugging)
# exec python manage.py runserver 0.0.0.0:8000

# Start Gunicorn
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000
