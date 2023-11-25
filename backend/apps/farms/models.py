from django.db import models
import uuid
from apps.abstracts.models import AbstractModel
import os
from apps.profiles.models import Profile

# Create your models here.


def get_upload_path(instance, filename):
    """
    This function is used to create a unique filename for each image uploaded to the server.
    :param instance: The instance parameter is the model instance that the file is attached to.
    :param filename: The filename parameter is the name of the file that was uploaded.
    :return: The function returns a string containing the path where the file will be saved.
    """
    return os.path.join("fotos", "granjas", str(instance.pk), filename)


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
    photo = models.ImageField(
        "Farms",
        upload_to=get_upload_path,
        default="granja.jpg",
        null=True,
        blank=True,
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
