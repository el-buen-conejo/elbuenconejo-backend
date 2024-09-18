# authentication/views.py

from dj_rest_auth.views import LoginView
from django.conf import settings
from django.http import HttpResponseRedirect
from rest_framework.permissions import AllowAny


def email_confirm_redirect(request, key):
    return HttpResponseRedirect(f"{settings.EMAIL_CONFIRM_REDIRECT_BASE_URL}{key}/")


def password_reset_confirm_redirect(request, uidb64, token):
    return HttpResponseRedirect(
        f"{settings.PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL}{uidb64}/{token}/"
    )


# Overwrite LoginView to allow access without authentication
class CustomLoginView(LoginView):
    permission_classes = [AllowAny]
