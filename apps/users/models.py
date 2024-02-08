from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from apps.abstracts.models import AbstractModel


class User(PermissionsMixin, AbstractBaseUser, AbstractModel):
    """
      It is a new model for custom user
    Args:
        username ( str ): knick name.
        email ( str ): email of the user
        is_staff ( bool ): is an user with permissions of the admin panel?
        is_active ( bool ): logic delete
        is_producer ( bool ): Is farmer or buyer

    """

    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=10, null=False, unique=True)
    email = models.EmailField(unique=True, null=False)
    is_staff = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    is_producer = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]
    objects = UserManager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
