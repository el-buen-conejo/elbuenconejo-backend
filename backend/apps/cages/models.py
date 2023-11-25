from django.db import models
from apps.farms.models import Farm
from apps.abstracts.models import AbstractModel
import os


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
    photo = models.ImageField(
        "Cages",
        upload_to=get_upload_path,
        default="jaula.jpg",
        null=True,
        blank=True,
    )
