import django_filters
from django_filters import rest_framework as filters
from tychy.models import Streets


class StreetFilter(django_filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")
    location = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Streets
        fields = "__all__"
