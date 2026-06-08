#!/usr/bin/env bash
set -euo pipefail

echo "Building the project..."

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m pip install -U python-dotenv pandas

echo "Making migrations..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collecting static files..."
python3 manage.py collectstatic --noinput --clear

echo "Build completed successfully."
