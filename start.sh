#!/bin/bash -v 
pip install -r requirements.txt

export SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex())')

# Create database tables
python manage.py migrate

# <module> is the name of the folder that contains wsgi.py
gunicorn --bind=0.0.0.0 --timeout 600 azureproject.wsgi