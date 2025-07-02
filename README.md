# Pet Clinic Django Project

## Overview

This project is a Django REST Framework (DRF) backend with Swagger API docs and a MySQL database running inside a Docker container.

---

## Setup Instructions

```

docker exec mysqldb mysqldump -u root -pwdm40! veterinary_ambulance > veterinary_ambulance.sql --no-tablespaces


mkdir pet_clinic
cd pet_clinic

python3 -m venv venv
source venv/bin/activate
pip install django djangorestframework drf-spectacular pymysql

mkdir backend
cd backend

django-admin startproject config .
django-admin startapp api

pet_clinic/
└── backend/
    ├── config/         # Django project folder (settings.py, urls.py)
    ├── api/            # Django app folder (models.py, views.py, urls.py)
    ├── manage.py
    └── venv/

import pymysql
pymysql.install_as_MySQLdb()

### config/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'veterinary_ambulance',
        'USER': 'youruser',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',  # Or Docker container IP/name
        'PORT': '3306',
    }
}

INSTALLED_APPS = [
    # ... other default apps ...
    'rest_framework',
    'drf_spectacular',
    'api',
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

### config/urls.py
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

### Create api/urls.py to handle your app-specific routes.

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Access:

Admin panel: http://localhost:8000/admin/

Swagger UI: http://localhost:8000/api/swagger/

Notes
MySQL runs inside a Docker container named mysqldb. Ensure network connectivity.

pymysql is installed and configured as MySQLdb driver replacement.

DRF Spectacular auto-generates API schema and Swagger UI.

### secure endpoints with JWT
pip install djangorestframework-simplejwt

### Update your settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',         # For browsable API (login via cookies)
        'rest_framework_simplejwt.authentication.JWTAuthentication',   # For Swagger + external clients (login via Bearer token)
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',  # keep your schema
}

### Swagger Page
http://localhost:8000/api/swagger/

### DRF Login Page
http://localhost:8000/api-auth/login/       # admin/wdm40!
http://localhost:8000/api/pets/
```
