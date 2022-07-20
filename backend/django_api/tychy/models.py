from django.db import models

# Create your models here.
class Flat(models.Model):
    link = models.SlugField(max_length=999)
    title = models.CharField(max_length=400, blank=True, null=True)
    localization = models.CharField(max_length=400, blank=True, null=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    rent = models.PositiveIntegerField(null=True, blank=True)
    rooms = models.PositiveIntegerField(null=True, blank=True)
    space = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=12, null=True, blank=True)

    # floor = models.BinaryField(null=True, blank=True)

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
    date = models.DateField(null=True, blank=True)

    district = models.CharField(max_length=20, null=True, blank=True)
    street = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.price} - {self.title} on {self.date}"


class Statistics(models.Model):
    flat_number = models.PositiveIntegerField(null=True, blank=True)
    flat_average_price = models.FloatField(null=True, blank=True)
    flat_average_rent = models.FloatField(null=True, blank=True)
    flat_m2_average_price = models.FloatField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)


    def __str__(self):
        return f"{self.date} - {self.flat_number}"

    class Meta:
        db_table = "flats_statistics"


class Districts(models.Model):
    location = models.CharField(max_length=300, null=True, blank=True)
    flat_number = models.PositiveIntegerField(null=True, blank=True)
    flat_average_price = models.FloatField(null=True, blank=True)
    flat_average_rent = models.FloatField(null=True, blank=True)
    flat_m2_average_price = models.FloatField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.date} - {self.location}"
    class Meta:
        db_table = "flats_districts"


class Streets(models.Model):
    location = models.CharField(max_length=300, null=True, blank=True)
    flat_number = models.PositiveIntegerField(null=True, blank=True)
    flat_average_price = models.FloatField(null=True, blank=True)
    flat_average_rent = models.FloatField(null=True, blank=True)
    flat_m2_average_price = models.FloatField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "flats_streets"
