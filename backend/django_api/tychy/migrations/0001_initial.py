# Generated by Django 4.0.5 on 2022-06-11 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Flat",
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
                ("title", models.CharField(blank=True, max_length=400, null=True)),
                (
                    "localization",
                    models.CharField(blank=True, max_length=400, null=True),
                ),
                ("price", models.PositiveIntegerField(blank=True, null=True)),
                ("rent", models.PositiveIntegerField(blank=True, null=True)),
                ("rooms", models.PositiveIntegerField(blank=True, null=True)),
                ("space", models.FloatField(blank=True, null=True)),
                ("status", models.CharField(blank=True, max_length=12, null=True)),
                ("floor", models.BinaryField(blank=True, null=True)),
                ("ownership", models.CharField(blank=True, max_length=51, null=True)),
                ("heating", models.CharField(blank=True, max_length=20, null=True)),
                ("car_park", models.BooleanField()),
                ("market", models.CharField(blank=True, max_length=17, null=True)),
                (
                    "advertiser_type",
                    models.CharField(blank=True, max_length=14, null=True),
                ),
                (
                    "type_of_building",
                    models.CharField(blank=True, max_length=11, null=True),
                ),
                ("elevator", models.BooleanField()),
                ("flat_window", models.CharField(blank=True, max_length=10, null=True)),
                ("build_year", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "building_material",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("date", models.DateField(blank=True, null=True)),
            ],
        ),
    ]
