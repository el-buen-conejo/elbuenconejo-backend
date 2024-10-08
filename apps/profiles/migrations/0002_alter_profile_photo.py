# Generated by Django 4.2.6 on 2024-09-18 16:31

import apps.profiles.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apps_profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="photo",
            field=models.URLField(
                default="/images/perfil.jpg",
                max_length=500,
                validators=[apps.profiles.models.file_validation],
            ),
        ),
    ]
