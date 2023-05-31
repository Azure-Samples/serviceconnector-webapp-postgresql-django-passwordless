#!/bin/bash -v 
pip install -r requirements.txt

export SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex())')

# Create database tables
python manage.py migrate