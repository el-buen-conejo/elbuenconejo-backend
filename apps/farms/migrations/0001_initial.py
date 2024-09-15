# Generated by Django 4.2.6 on 2024-09-15 03:03

import apps.farms.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Farm",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        db_index=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                ("name", models.CharField(max_length=150)),
                ("address", models.CharField(max_length=150)),
                ("description", models.TextField(max_length=200)),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        default="granja.jpg",
                        null=True,
                        upload_to=apps.farms.models.get_upload_path,
                        verbose_name="Farms",
                    ),
                ),
            ],
            options={
                "verbose_name": "farm",
                "verbose_name_plural": "farm",
                "db_table": "farm",
                "ordering": ["name"],
            },
        ),
    ]
