# Social Media API (initial auth)

## Setup
1. Create virtualenv and install:
   pip install -r requirements.txt

2. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

3. Create admin:
   python manage.py createsuperuser

4. Start:
   python manage.py runserver

## Endpoints
- POST /api/accounts/register/  — register (returns token)
- POST /api/accounts/login/     — login (returns token + user)
- GET/PUT /api/accounts/profile/ — get/update profile (requires token)

Use header:
Authorization: Token <token>
