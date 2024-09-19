import os

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from django.db import models

from apps.abstracts.models import AbstractModel
from apps.profiles.models import Profile

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
    return os.path.join("fotos", "jaulas", str(instance.pk), filename)


class Farm(AbstractModel):
    """
      It is a place where the farmer care their animals and
      manage them for trade.
    Args:
        name ( str ): farm name.
        address ( str ): farm address
        is_active ( bool ): logic delete
    """

    name = models.CharField(max_length=150, blank=False)
    address = models.CharField(max_length=150, blank=False)
    description = models.TextField(max_length=200)
    photo = models.URLField(
        validators=[file_validation], default="/images/granja.jpg", max_length=500
    )
    profile_id = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="profile_farm"
    )

    # Modifica como se visualiza el nombre de la clase en el admin
    # Como ordenar los datos en el admin
    class Meta:
        db_table = "farm"
        verbose_name = "farm"
        verbose_name_plural = "farm"
        ordering = ["name"]

    def __str__(self):
        return f"{self.id} {self.name} {self.address} {self.is_active}"
