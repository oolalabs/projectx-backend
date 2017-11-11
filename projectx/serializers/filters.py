from rest_framework import serializers
from projectx.models.filters import *


class HashTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashTag
        fields = ('__all__')


class HashTagLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashTagLink
        fields = ('__all__')