from django.http import HttpResponse
from tychy.models import Flat, Statistics
from datetime import date


def remove_flats(request):
    queryset = Flat.objects.filter(date=date.today())
    for i in queryset:
        i.delete()

    stats = Statistics.objects.get(date=date.today())
    stats.delete()

    return HttpResponse("Deleted")
