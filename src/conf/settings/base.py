"""
Django settings for coin_exchange project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
import datetime
import logging
import sys
from os.path import abspath, basename, dirname, join, normpath
from sentry_sdk.integrations.logging import LoggingIntegration

DJANGO_ROOT = dirname(dirname(abspath(__file__)))
SITE_ROOT = dirname(DJANGO_ROOT)
SITE_NAME = basename(DJANGO_ROOT)
sys.path.append(DJANGO_ROOT)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = dirname(DJANGO_ROOT)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*jd1cgw&5$oplh@zb7+d!!_^v#98ng3c5*qrz%skj(9hn7w4p%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEST = True
UNIT_TEST = False

ALLOWED_HOSTS = []

SYSTEM_TOKEN = 'xxx'

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'django_filters',
    'tinymce',
]

LOCAL_APPS = [
    'sdk',
    'constant_core'
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

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

WSGI_APPLICATION = 'conf.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))
MEDIA_URL = '/media/'
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'common.http.custom_exception_handler',
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'sdk_auth.authentication.SdkAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=60*60)
}

CORS_ORIGIN_ALLOW_ALL = True

TINYMCE_DEFAULT_CONFIG = {
    'width': '80%',
    'height': '300px'
}

# All of this is already happening by default!
sentry_logging = LoggingIntegration(
    level=logging.INFO,        # Capture info and above as breadcrumbs
    event_level=logging.ERROR  # Send errors as events
)

EMAIL_FROM_NAME = 'The Constant Foundation'
EMAIL_FROM_ADDRESS = "annie@myconstant.com"

CONST_EXCHANGE_API = {
    'URL': 'https://staging.constant.money/exchange-api/exchange-job',
    'TOKEN': 'ypaEye4bhUnnKkWQAEPmVzs8Wnt2yh2U2TwACePXYqR8nxmD',
}