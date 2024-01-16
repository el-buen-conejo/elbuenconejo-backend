# Generated by Django 4.2.6 on 2024-01-16 02:50

import apps.rabbits.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("apps_cages", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Rabbit",
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
                (
                    "breed",
                    models.CharField(
                        choices=[
                            ("Azteca", "Azteca"),
                            ("Cabeza de León", "Cabeza de León"),
                            ("California", "California"),
                            ("Chinchilla", "Chinchilla"),
                            ("Gigante de Flandes", "Gigante de Flandes"),
                            ("Mariposa", "Mariposa"),
                            ("Nueva Zelanda", "Nueva Zelanda"),
                            ("Rex", "Rex"),
                            ("Otro", "Otro"),
                        ],
                        default="Especie",
                    ),
                ),
                (
                    "genre",
                    models.CharField(
                        choices=[("Macho", "Macho"), ("Hembra", "Hembra")],
                        default="Genero",
                    ),
                ),
                ("birthday", models.DateField(default=django.utils.timezone.now)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=7),
                ),
                ("tag", models.CharField(max_length=15, unique=True)),
                (
                    "weight",
                    models.DecimalField(decimal_places=1, default=1, max_digits=3),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        default="conejo.jpg",
                        null=True,
                        upload_to=apps.rabbits.models.get_upload_path,
                        verbose_name="Rabbits",
                    ),
                ),
                (
                    "cage_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rabbits",
                        to="apps_cages.cage",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
