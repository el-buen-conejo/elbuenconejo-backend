import os
import csv
from apps.catalogs.models import City
from apps.catalogs.models import State
from apps.addresses.models import Address
from django.db import connection
from utils.mixin_classes.mixin_class import ResetAutoIncrementMixin


class ExecuteSqlAddress(ResetAutoIncrementMixin):
    def __init__(self, env_variable, path_to_csv_file):
        self.env_variable = env_variable
        self.path_to_csv_file = path_to_csv_file

    def csv_file_name(self):
        self.reset_auto_increment(self.env_variable)

        with open(self.path_to_csv_file) as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                print(f"Added Tuple: CITY_ID ==> {row[5]} STATE_ID => {row[6]}")
                addresses = Address(
                    id=row[0],
                    created=row[1],
                    updated=row[2],
                    is_active=row[3],
                    address=row[4],
                    city=City.objects.get(id=row[5]),
                    state=State.objects.get(id=row[6]),
                )
                addresses.save()
