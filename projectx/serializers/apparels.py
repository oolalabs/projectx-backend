from rest_framework import serializers
from projectx.models.apparels import *


class ApparelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApparelType
        fields = ('__all__')


class ApparelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apparel
        fields = ('__all__')


class ApparelTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApparelTag
        fields = ('__all__')