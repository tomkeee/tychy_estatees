import django_filters
from django_filters import rest_framework as filters
from tychy.models import Districts


class DistrictFilter(django_filters.FilterSet):
    location = filters.CharFilter()
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Districts
        fields = ("flat_average_price",)
