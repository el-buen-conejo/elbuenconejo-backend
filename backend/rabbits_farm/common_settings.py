"""
Django settings for rabbits_farm project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
import environ
import os

# from utils.get_parameters_store.parameter_store import get_parameter

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)
# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
print("E U R E K A -- BASE_DIR: " + os.path.join(BASE_DIR, ".env"))

# False if not in os.environ because of casting above
DEBUG = env("DEBUG")
print(" RED PILL:", DEBUG)
# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env("SECRET_KEY")


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}

AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")


# Application definition


# Applications core of Django
BASE_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

# Local applications
LOCAL_APPS = [
    "apps.users",
    "apps.farms",
    "apps.rabbits",
    "apps.cages",
    "apps.profiles",
    "apps.markets",
    "apps.catalogs",
    "apps.addresses",
    "apps.authentication",
]

# Third persons applications
THIRD_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    # "rest_framework_simplejwt.token_blacklist",
    "django_filters",
    "drf_spectacular",
    "django_extensions",
    "corsheaders",
    "storages",
    "whitenoise.runserver_nostatic",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # "allauth.socialaccount.providers.google",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "zappa_django_utils",
    "drf_standardized_errors",
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

ROOT_URLCONF = "rabbits_farm.urls"

SITE_ID = 1  # make sure SITE_ID is set

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "rabbits_farm.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# For specific the new user model
AUTH_USER_MODEL = "users.User"

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "es-mx"

TIME_ZONE = "America/Mexico_City"

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

# se desactivo la consta de abajo para que Django no genere el
# id de manera automática.

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DRF_STANDARDIZED_ERRORS = {"ENABLE_IN_DEBUG_FOR_UNHANDLED_EXCEPTIONS": True}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    # "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    # "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_SCHEMA_CLASS": "drf_standardized_errors.openapi.AutoSchema",
    "EXCEPTION_HANDLER": "drf_standardized_errors.handler.exception_handler",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": True,
    "SIGNING_KEY": "complexsigningkey",  # generate a key and replace me
    "ALGORITHM": "HS512",
}

REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_HTTPONLY": False,
}

SPECTACULAR_SETTINGS = {
    "TITLE": "El Buen Conejo API",
    "DESCRIPTION": "API para la plataforma del Buen Conejo",
    "VERSION": "2.0.0",
    "SERVE_INCLUDE_SCHEMA": True,
    "COMPONENT_SPLIT_REQUEST": True,
    "SCHEMA_PATH_PREFIX_INSERT": "/staging",
    # OTHER SETTINGS
    "ENUM_NAME_OVERRIDES": {
        "ValidationErrorEnum": "drf_standardized_errors.openapi_serializers.ValidationErrorEnum.choices",
        "ClientErrorEnum": "drf_standardized_errors.openapi_serializers.ClientErrorEnum.choices",
        "ServerErrorEnum": "drf_standardized_errors.openapi_serializers.ServerErrorEnum.choices",
        "ErrorCode401Enum": "drf_standardized_errors.openapi_serializers.ErrorCode401Enum.choices",
        "ErrorCode403Enum": "drf_standardized_errors.openapi_serializers.ErrorCode403Enum.choices",
        "ErrorCode404Enum": "drf_standardized_errors.openapi_serializers.ErrorCode404Enum.choices",
        "ErrorCode405Enum": "drf_standardized_errors.openapi_serializers.ErrorCode405Enum.choices",
        "ErrorCode406Enum": "drf_standardized_errors.openapi_serializers.ErrorCode406Enum.choices",
        "ErrorCode415Enum": "drf_standardized_errors.openapi_serializers.ErrorCode415Enum.choices",
        "ErrorCode429Enum": "drf_standardized_errors.openapi_serializers.ErrorCode429Enum.choices",
        "ErrorCode500Enum": "drf_standardized_errors.openapi_serializers.ErrorCode500Enum.choices",
    },
    "POSTPROCESSING_HOOKS": [
        "drf_standardized_errors.openapi_hooks.postprocess_schema_enums"
    ],
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Provider specific settings
# SOCIALACCOUNT_PROVIDERS = {
#     "google": {
#         # For each OAuth based provider, either add a ``SocialApp``
#         # (``socialaccount`` app) containing the required client
#         # credentials, or list them here:
#         "APP": {"client_id": "123", "secret": "456", "key": ""}
#     }
# }

ACCOUNT_AUTHENTICATION_METHOD = "username"
# The user is required to hand over an e-mail address when signing up.
ACCOUNT_EMAIL_REQUIRED = True

# Determines the e-mail verification method during signup. When set to
# "mandatory" the user is blocked from logging in until the email
# address is verified. Choose "optional" or "none" to allow logins
# with an unverified e-mail address. In case of "optional", the e-mail
# verification mail is still sent, whereas in case of "none" no e-mail
# verification mails are sent.
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

# <EMAIL_CONFIRM_REDIRECT_BASE_URL>/<key>
EMAIL_CONFIRM_REDIRECT_BASE_URL = "http://localhost:3000/email/confirm/"

# <PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL>/<uidb64>/<token>/
PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL = (
    "http://localhost:3000/password-reset/confirm/"
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "staticfiles/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_URLS = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# Configuration of environment variables for setup static files in a S3 bucket

AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_SIGNATURE_NAME = env("AWS_S3_SIGNATURE_NAME")
AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME")
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "staticfiles": {
        # "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
}

# # Correo electrónico
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("SMTP_SERVER")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_USE_SSL = True
EMAIL_HOST_USER = env("EMAIL_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD")
DEFAULT_FROM_EMAIL = env("FROM_EMAIL")

if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
else:
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:3000/",
        "http://127.0.0.1:3000/",
    ]
