"""
Django settings for LibTrade project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
from django.contrib import messages
import os
import django_heroku
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR , 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r3%-c1#7s=9yn(^r$v6wdex1(ytfmj@ovv0tu58dl&o@*2fm00'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'accounts',
    'taggit',
    'bootstrap4',
    'crispy_forms',
    'storages',
]

SITE_ID = 1

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LibTrade.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                TEMPLATES_DIR,
        ],
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

WSGI_APPLICATION = 'LibTrade.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# <<<<<<< HEAD
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'libtraddb',
#         'USER':'postgres',
#         'PASSWORD':'@@sai@@@',
#         'HOST': 'localhost',
#         'port': 5432,
# =======

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Custom Django auth settings
AUTH_USER_MODEL = 'accounts.User'

LOGIN_URL = 'login'

LOGOUT_URL = 'logout'

LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = 'landing'



# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
# email stuff

EMAIL_HOST = 'smpt.gmail.com'
EMAIL_HOST_USER = '****'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = '****'
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = '****'


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_ROOT =  os.path.join(BASE_DIR, 'assets')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# email_conn = smtplib.SMTP(host, port)
# email_conn.starttls()
# email_conn.login(username, password)
# >> import smtplib
# >>> host = "smtp.gmail.com"
# >>> port = 587
# >>> username = "@gmail.com"
# >>> password = ""
# >>>
# >>> email_conn = smtplib.SMTP(host, port)
# >>> email_conn.ehlo()
# (250, b'smtp.gmail.com at your service, [2001:8f8:162d:6854:b02f:a8b7:5a29:ac9b]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
# >>> email_conn.starttls()
# (220, b'2.0.0 Ready to start TLS')
# >>> email_conn.login(username, password)
# (235, b'2.7.0 Accepted')
# >>> email_conn.sendmail(username, [username],"helo helo" )
# {}
# EMAIL_USE_TSL = True
# EMAIL_HOST =  'smpt.gmail.com'
# EMAIL_HOST_USER = '@gmail.com'
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT = 587
