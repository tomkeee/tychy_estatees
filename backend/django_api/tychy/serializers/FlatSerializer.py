from rest_framework import serializers
from tychy.models import Flat


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = "__all__"
