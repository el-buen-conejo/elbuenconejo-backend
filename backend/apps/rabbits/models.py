from django.db import models
from apps.cages.models import Cage
from apps.abstracts.models import AbstractModel
from django.utils import timezone
import os


def get_upload_path(instance, filename):
    """
    This function is used to create a unique filename for each image uploaded to the server.
    :param instance: The instance parameter is the model instance that the file is attached to.
    :param filename: The filename parameter is the name of the file that was uploaded.
    :return: The function returns a string containing the path where the file will be saved.
    """
    return os.path.join("fotos", "conejos", str(instance.pk), filename)


# Create your models here.
class Rabbit(AbstractModel):
    """
    The animal of the farm for trade.

    Args:
        cage_id (str): related with cage model
        breed (str): breed of the rabbit
        genre (str): genre of the rabbit
        price (decimal): public price for trade
        tag (str): identifier od the rabbit
        weight (decimal): weight of the rabbit
        is_active (boolean): logic delete

    """

    BREED_CHOICE = (
        ("Azteca", "Azteca"),
        ("Cabeza de León", "Cabeza de León"),
        ("California", "California"),
        ("Chinchilla", "Chinchilla"),
        ("Gigante de Flandes", "Gigante de Flandes"),
        ("Mariposa", "Mariposa"),
        ("Nueva Zelanda", "Nueva Zelanda"),
        ("Rex", "Rex"),
        ("Otro", "Otro"),
    )
    GENDER_CHOICE = (
        ("Macho", "Macho"),
        ("Hembra", "Hembra"),
    )

    cage_id = models.ForeignKey(Cage, on_delete=models.CASCADE, related_name="rabbits")
    breed = models.CharField(choices=BREED_CHOICE, blank=False, default="Especie")
    genre = models.CharField(choices=GENDER_CHOICE, blank=False, default="Genero")
    birthday = models.DateField(null=False, blank=False, default=timezone.now)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    tag = models.CharField(max_length=15, unique=True, blank=False)
    weight = models.DecimalField(max_digits=3, decimal_places=1, default=1)
    photo = models.ImageField(
        "Rabbits",
        upload_to=get_upload_path,
        default="conejo.jpg",
        null=True,
        blank=True,
    )
