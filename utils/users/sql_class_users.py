import os
import csv
from apps.users.models import User
from django.db import connection


class ExecuteSqlSentence:
    def __init__(self, variable):
        self.variable = variable

    def reset_autoincrement_sql(self):
        sql_result = os.environ.get(self.variable)
        return sql_result.replace(",", " ")

    def csv_file_name(self, filename):
        with open(filename) as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                print(row)
                users = User(
                    password=row[0],
                    last_login=row[1],
                    is_superuser=row[2],
                    id=row[3],
                    username=row[4],
                    email=row[5],
                    is_staff=row[6],
                    is_active=row[7],
                )
                users.save()

    def reset_auto_increment_users(self):
        with connection.cursor() as cursor:
            cursor.execute(self.reset_autoincrement_sql())
