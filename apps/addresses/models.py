from django.db import models
from apps.abstracts.models import AbstractModel
from apps.catalogs.models import State, City


# Create your models here.
class Address(AbstractModel):
    address = models.CharField(max_length=150)
    state = models.ForeignKey(
        State, on_delete=models.CASCADE, related_name="state_address"
    )
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="city_address"
    )

    def __str__(self):
        return self.address

    class Meta:
        db_table = "addresses"
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"
