import os

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from django.db import models

from apps.addresses.models import Address
from apps.users.models import User

# For testing model validation
FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 10  # 10mb


def file_validation(file):
    if not file:
        raise ValidationError("No file selected.")

    # For regular upload, we get UploadedFile instance, so we can validate it.
    # When using direct upload from the browser, here we get an instance of the CloudinaryResource
    # and file is already uploaded to Cloudinary.
    # Still can perform all kinds on validations and maybe delete file, approve moderation, perform analysis, etc.
    if isinstance(file, UploadedFile):
        if file.size > FILE_UPLOAD_MAX_MEMORY_SIZE:
            raise ValidationError("File shouldn't be larger than 10MB.")


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
     The Profile is extended user data.

    Args:
        user_id ( str ): related with user model
        is_producer ( coolean ): productor or user
        qualifications ( float ): average of the grades obtained
        is_active ( boolean ): logic delete.
    """

    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    address_id = models.OneToOneField(
        Address, on_delete=models.CASCADE, blank=True, null=True
    )
    qualification = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    # photo = CloudinaryField(
    #     "image", validators=[file_validation], default="utils/images/perfil.jpg"
    # )
    photo = models.URLField(
        validators=[file_validation], default="/images/perfil.jpg", max_length=500
    )
    saw_tutorial = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
