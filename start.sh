#!/bin/bash
python manage.py collectstatic --no-input
python manage.py migrate --no-input
daphne oc_lettings_site.asgi:application -p 8000 -b 0.0.0.0
echo "Current directory: $(pwd)"
echo "Contents of /app: $(ls -la /app)"