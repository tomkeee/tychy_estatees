from rest_framework import serializers
from tychy.models import Streets


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Streets
        fields = "__all__"
