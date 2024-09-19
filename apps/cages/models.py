import os

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from django.db import models

from apps.abstracts.models import AbstractModel
from apps.farms.models import Farm

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


# Create your models here.
class Cage(AbstractModel):
    """
    The Cage is used to keep the rabbits.
    One cage has one or many rabbits.

    Args:
        farm_id ( str ): related with farm model
        count_rabbits ( int ): the total rabbits kepped into cage.
        price ( decimal ): public price
        is_public ( boolean ): the farm decide if customers can see the cage.
        is_active ( boolean ): logic delete.
    """

    farm_id = models.ForeignKey(Farm, on_delete=models.CASCADE)
    count_rabbits = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    is_public = models.BooleanField(default=False)
    total_weight = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    photo = models.URLField(
        validators=[file_validation], default="/images/granja.jpg", max_length=500
    )
