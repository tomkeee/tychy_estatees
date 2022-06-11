from datetime import date

from tychy.models import Flat
from tychy.serializers.FlatSerializer import FlatSerializer
from tychy.filters.FlatFilter import FlatFilter
from rest_framework import generics


class FlatListAll(generics.ListAPIView):
    serializer_class = FlatSerializer

    def get_queryset(self):
        return Flat.objects.all()


class FlatListToday(generics.ListAPIView):
    serializer_class = FlatSerializer

    def get_queryset(self):
        return Flat.objects.filter(date=date.today())


class FlatListFilter(generics.ListAPIView):
    serializer_class = FlatSerializer

    def get_queryset(self):
        return Flat.objects.filter(date=date.today())

    def filter_queryset(self, queryset):
        query_params = self.request.query_params

        qs = FlatFilter(
            queryset=queryset,
            data=self.request.query_params,
            request=self.request,
        ).qs

        return qs
