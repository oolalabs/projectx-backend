from rest_framework import serializers
from projectx.models.activities import *


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('__all__')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('__all__')


class SaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Save
        fields = ('__all__')