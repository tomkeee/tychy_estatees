from rest_framework import serializers
from tychy.models import Districts


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Districts
        fields = "__all__"
