from django.db import models

# Create your models here.
class Flat(models.Model):
    link = None
    title = models.CharField(max_length=400, blank=True, null=True)
    localization = models.CharField(max_length=400, blank=True, null=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    rent = models.PositiveIntegerField(null=True, blank=True)
    rooms = models.PositiveIntegerField(null=True, blank=True)
    space = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=12, null=True, blank=True)
    floor = models.JSONField(null=True, blank=True)
    ownership = models.CharField(max_length=51, null=True, blank=True)
    heating = models.CharField(max_length=20, null=True, blank=True)
    car_park = models.BooleanField()
    # additionals
    market = models.CharField(max_length=17, null=True, blank=True)
    advertiser_type = models.CharField(max_length=14, null=True, blank=True)
    type_of_building = models.CharField(max_length=11, null=True, blank=True)
    elevator = models.BooleanField()
    flat_window = models.CharField(max_length=10, null=True, blank=True)
    # flat_media = models.CharField()
    build_year = models.PositiveIntegerField(null=True, blank=True)
    building_material = models.CharField(max_length=20, null=True, blank=True)
