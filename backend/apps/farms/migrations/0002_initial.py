# Generated by Django 4.2.6 on 2024-01-20 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("apps_profiles", "0001_initial"),
        ("apps_farms", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="farm",
            name="profile_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="profile_farm",
                to="apps_profiles.profile",
            ),
        ),
    ]
