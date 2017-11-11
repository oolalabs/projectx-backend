from rest_framework import serializers
from projectx.models.outfits import *


class OutfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outfit
        fields = ('__all__')


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('__all__')