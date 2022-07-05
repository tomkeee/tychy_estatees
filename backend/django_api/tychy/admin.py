from django.contrib import admin

from tychy.models import Flat, Statistics,Districts,Streets

# Register your models here.

admin.site.register(Flat)
admin.site.register(Districts)
admin.site.register(Streets)
admin.site.register(Statistics)
