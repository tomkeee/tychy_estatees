from rest_framework.response import Response
from rest_framework import views, generics

from datetime import date

from tychy.serializers.DistrictSerializer import DistrictSerializer
from tychy.serializers.StreetSerializer import StreetSerializer
from tychy.serializers.FlatSerializer import FlatSerializer
from tychy.serializers.StatisticsSerializer import StatisticsSerializer

from tychy.models import Flat, Statistics, Streets, Districts

from tychy.filters.FlatFilter import FlatFilter
from tychy.filters.StreetFilter import StreetFilter
from tychy.filters.DistrictFilter import DistrictFilter


class FlatListAll(generics.ListAPIView):
    serializer_class = FlatSerializer

    def get_queryset(self):
        return Flat.objects.all()


class FlatListToday(generics.ListAPIView):
    serializer_class = FlatSerializer

    def get_queryset(self):
        return Flat.objects.filter(date=date.today())

    def filter_queryset(self, queryset):
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
        ordered_queryset = queryset.order_by("date")
        return ordered_queryset


class StatisticsListToday(generics.ListAPIView):
    serializer_class = StatisticsSerializer

    def get_queryset(self):
        queryset = Statistics.objects.filter(date=date.today())
        ordered_queryset = queryset.order_by("-date")
        return ordered_queryset


class DistrictListView(generics.ListAPIView):
    serializer_class = DistrictSerializer
    queryset = Districts.objects.all()

    def filter_queryset(self, queryset):
        qs = DistrictFilter(
            queryset=queryset,
            data=self.request.query_params,
            request=self.request,
        ).qs

        return qs


class StreetListView(generics.ListAPIView):
    serializer_class = StreetSerializer
    queryset = Streets.objects.all()

    def filter_queryset(self, queryset):
        qs = StreetFilter(
            queryset=queryset,
            data=self.request.query_params,
            request=self.request,
        ).qs

        return qs


class StreetList(views.APIView):
    def get(self, request):
        streets = set(
            street.lower().capitalize()
            for street in Streets.objects.values_list("location", flat=True)
        )

        return Response(sorted(streets))
