# Generated by Django 4.2.6 on 2024-02-01 04:35

import apps.profiles.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0001_initial"),
        ("apps_addresses", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "user_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
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
