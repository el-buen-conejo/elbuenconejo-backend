# Generated by Django 4.2.6 on 2023-12-13 01:59

import apps.profiles.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("apps_addresses", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("is_producer", models.BooleanField(default=False)),
                ("first_name", models.CharField(blank=True, max_length=50, null=True)),
                ("last_name", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "qualification",
                    models.DecimalField(decimal_places=2, default=0, max_digits=5),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        default="perfil.jpg",
                        null=True,
                        upload_to=apps.profiles.models.get_upload_path,
                        verbose_name="Profiles",
                    ),
                ),
                ("saw_tutorial", models.BooleanField(default=False)),
                (
                    "address_id",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apps_addresses.address",
                    ),
                ),
            ],
            options={
                "verbose_name": "Perfil",
                "verbose_name_plural": "Perfiles",
            },
        ),
    ]
