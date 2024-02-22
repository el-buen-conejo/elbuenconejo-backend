import os
import csv
from apps.addresses.models import Address
from apps.profiles.models import Profile
from apps.users.models import User
from django.db import connection
from utils.mixin_classes.mixin_class import ResetAutoIncrementMixin


class ExecuteSqlProfile(ResetAutoIncrementMixin):
    def __init__(self, env_variable, path_to_csv_file):
        self.env_variable = env_variable
        self.path_to_csv_file = path_to_csv_file

    def csv_file_name(self):
        self.reset_auto_increment(self.env_variable)

        with open(self.path_to_csv_file) as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                print(f"Added Tuple: ADRESS_ID ==> {row[9]} USER_ID => {row[10]}")
                profiles = Profile(
                    id=row[0],
                    is_producer=row[1],
                    first_name=row[2],
                    last_name=row[3],
                    photo=row[4],
                    qualification=row[5],
                    is_active=row[6],
                    created=row[7],
                    updated=row[8],
                    address_id=Address.objects.get(id=row[9]),
                    user_id=User.objects.get(id=row[10]),
                )
                profiles.save()
