import os
import csv
from apps.catalogs.models import State
from django.db import connection
from utils.mixin_classes.mixin_class import ResetAutoIncrementMixin


class ExecuteSqlStates(ResetAutoIncrementMixin):
    def __init__(self, env_variable, path_to_csv_file):
        self.env_variable = env_variable
        self.path_to_csv_file = path_to_csv_file

    def csv_file_name(self):
        self.reset_auto_increment(self.env_variable)

        with open(self.path_to_csv_file) as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                print(row)
                states = State(
                    id=row[0],
                    created=row[1],
                    updated=row[2],
                    is_active=row[3],
                    state=row[4],
                )
                states.save()
