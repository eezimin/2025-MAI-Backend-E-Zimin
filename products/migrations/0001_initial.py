# Generated by Django 5.0 on 2025-03-03 11:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("calories", models.PositiveIntegerField()),
                ("protein", models.FloatField()),
                ("fat", models.FloatField()),
                ("carbs", models.FloatField()),
            ],
        ),
    ]
