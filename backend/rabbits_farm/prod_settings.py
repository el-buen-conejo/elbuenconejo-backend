from .common_settings import *

# This code is for production
# If exists environemnt variable AWS_EXTERNAL_HOSTNAME then append element in ALLOWED_HOSTS list and DEBUG is False

ALLOWED_HOSTS = ["107.21.219.35", "apiebc.online"]

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
