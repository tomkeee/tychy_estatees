from datetime import date

from tychy.models import Flat, Statistics
from tychy.serializers.FlatSerializer import FlatSerializer
from tychy.serializers.StatisticsSerializer import StatisticsSerializer

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


class StatisticsListAll(generics.ListAPIView):
    serializer_class = StatisticsSerializer

    def get_queryset(self):
        queryset = Statistics.objects.all()
        ordered_queryset = queryset.order_by("-date")
        return ordered_queryset


class StatisticsListToday(generics.ListAPIView):
    serializer_class = StatisticsSerializer

    def get_queryset(self):
        queryset = Statistics.objects.filter(date=date.today())
        ordered_queryset = queryset.order_by("-date")
        return ordered_queryset
