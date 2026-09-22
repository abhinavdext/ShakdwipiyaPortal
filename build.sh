#!/usr/bin/env bash
set -o errexit

python manage.py collectstatic --no-input
python manage.py migrate

python manage.py shell -c "
import os
from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get('ADMIN_USERNAME')
password = os.environ.get('ADMIN_PASSWORD')

if username and password:
    user, created = User.objects.get_or_create(
        username=username
    )
    user.is_staff = True
    user.is_superuser = True
    user.set_password(password)
    user.save()
    print('Admin user created/updated successfully.')
else:
    print('ADMIN_USERNAME or ADMIN_PASSWORD not set.')
"