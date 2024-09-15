# Generated by Django 4.2.6 on 2024-09-15 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("apps_cages", "0001_initial"),
        ("apps_farms", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cage",
            name="farm_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="apps_farms.farm"
            ),
        ),
    ]
