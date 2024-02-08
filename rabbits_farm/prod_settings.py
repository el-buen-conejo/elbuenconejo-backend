from .common_settings import *

# This code is for production
# If exists environemnt variable AWS_EXTERNAL_HOSTNAME then append element in ALLOWED_HOSTS list and DEBUG is False

ALLOWED_HOSTS = ["34.236.44.132"]
# ALLOWED_HOSTS.append(env("AWS_EXTERNAL_HOSTNAME"))

DEBUG = False

# Configuration of django-cors-headers
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

MIDDLEWARE.append("whitenoise.middleware.WhiteNoiseMiddleware")

# CORS_ALLOWED_ORIGINS = [
#     "*",  # Agrega los dominios permitidos aquí
# ]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]
