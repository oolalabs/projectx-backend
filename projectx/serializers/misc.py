from rest_framework import serializers
from projectx.models.misc import *


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('__all__')