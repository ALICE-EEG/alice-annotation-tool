"""
Django settings for drf_backend project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from os.path import join
from pathlib import Path

import matplotlib
matplotlib.use('Agg')


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

if 'DJANGO_ENVIRONMENT' in os.environ and os.environ['DJANGO_ENVIRONMENT'] == 'prod':
    env = 'prod'
else:
    env = 'dev'


if env == 'prod':
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
else:
    SECRET_KEY = '*udtpxl4zo*0cy204%@kkag)!hr(drh_uzljyrfjl(+fvwf$=#'
    DEBUG = True

ALLOWED_HOSTS = ['168.119.186.83', 'localhost', '127.0.0.1', 'alice.adase.org', 'alice.appliedai.tech']
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:8080',
    'http://168.119.186.83:8080',
    'http://168.119.186.83:80',
]
if env == 'prod':
    CUSTOM_HOST = 'http://alice.appliedai.tech'
else:
    CUSTOM_HOST = 'http://localhost:3000'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'django_filters',
    'django_rest_passwordreset',
    'data_app',
    'main_app',
    'auth_app',
    'downloads_app'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'drf_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'drf_backend.wsgi.application'


if env == 'prod':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': os.environ['DJANGO_POSTGRES_PASSWORD'],
            'HOST': os.environ['DJANGO_POSTGRES_HOST'],
            'PORT': os.environ['DJANGO_POSTGRES_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'pwd',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

if env == 'prod':
    STATIC_ROOT = '/django_static/api-static'
    MEDIA_ROOT = '/django_media/media'
    OUT_DIR = '/django_out'
else:
    STATIC_ROOT = join(BASE_DIR, 'static')
    MEDIA_ROOT = join(BASE_DIR, 'media')
    OUT_DIR = join(BASE_DIR, 'out')

STATIC_URL = '/api-static/'
MEDIA_URL = '/media/'
TMP_DIR = join(BASE_DIR, 'tmp')


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ],
}

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'aliceadase@gmail.com'
EMAIL_HOST_PASSWORD = os.environ['DJANGO_EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = True

# Logging
if env == 'prod':
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': '/logs/info.log',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'INFO',
                'propagate': True,
            },
        },
    }


if env == 'prod':
    CELERY_BROKER_URL = "redis://redis:6379/0"
else:
    CELERY_BROKER_URL = "redis://localhost:6379/0"

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]
