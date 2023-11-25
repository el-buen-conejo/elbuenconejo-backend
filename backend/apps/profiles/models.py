from django.db import models
import uuid
from apps.users.models import User
from apps.addresses.models import Address
import os


def get_upload_path(instance, filename):
    """
    This function is used to create a unique filename for each image uploaded to the server.
    :param instance: The instance parameter is the model instance that the file is attached to.
    :param filename: The filename parameter is the name of the file that was uploaded.
    :return: The function returns a string containing the path where the file will be saved.
    """
    return os.path.join("fotos", "perfiles", str(instance.pk), filename)


# Create your models here.
class Profile(models.Model):
    """
     The Profile is extended user date.

    Args:
        user_id ( str ): related with user model
        is_producer ( coolean ): productor or user
        qualifications ( float ): average of the grades obtained
        is_active ( boolean ): logic delete.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    is_producer = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    address_id = models.OneToOneField(
        Address, on_delete=models.CASCADE, blank=True, null=True
    )
    qualification = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(
        "Profiles",
        upload_to=get_upload_path,
        default="perfil.jpg",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
