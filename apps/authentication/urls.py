# authentication/urls.py

from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import (
    RegisterView,
    ResendEmailVerificationView,
    VerifyEmailView,
)
from dj_rest_auth.views import (
    LogoutView,
    PasswordResetConfirmView,
    PasswordResetView,
)
from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView

from apps.authentication.views import (
    email_confirm_redirect,
    password_reset_confirm_redirect,
)

from .views import CustomLoginView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", CustomLoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    # path("user/", UserDetailsView.as_view(), name="rest_user_details"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("token/refresh/", get_refresh_view().as_view(), name="token_refresh"),
    path("register/verify-email/", VerifyEmailView.as_view(), name="rest_verify_email"),
    path(
        "register/resend-email/",
        ResendEmailVerificationView.as_view(),
        name="rest_resend_email",
    ),
    path(
        "account-confirm-email/<str:key>/",
        email_confirm_redirect,
        name="account_confirm_email",
    ),
    path(
        "account-confirm-email/",
        VerifyEmailView.as_view(),
        name="account_email_verification_sent",
    ),
    path("password/reset/", PasswordResetView.as_view(), name="rest_password_reset"),
    path(
        "password/reset/confirm/<str:uidb64>/<str:token>/",
        password_reset_confirm_redirect,
        name="password_reset_confirm",
    ),
    path(
        "password/reset/confirm/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]
