from dataclasses import field
import django_filters
from django_filters import rest_framework as filters
from tychy.models import Flat


class FlatFilter(django_filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Flat
        fields = "__all__"
