from django.http import HttpResponse
from tychy.models import Flat, Statistics, Districts, Streets
from datetime import date


def remove_flats(request):
    queryset = Flat.objects.filter(date=date.today())
    for i in queryset:
        i.delete()

    stats = Statistics.objects.filter(date=date.today())
    for i in stats:
        i.delete()

    districts = Districts.objects.filter(date=date.today())
    for i in districts:
        i.delete()

    streets = Streets.objects.filter(date=date.today())
    for i in streets:
        i.delete()

    return HttpResponse("Deleted")
