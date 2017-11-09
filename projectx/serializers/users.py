from rest_framework import serializers
from projectx.models import *


class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ('id', 'first_name', 'last_name', 'email',
                  'phone_number', 'username', 'password')

    password = serializers.CharField(write_only=True)
    email = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def create(self, validated_data):
        try:
            user = MainUser(
                username = validated_data['username'],
                email = validated_data['email'],
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name'],
                phone_number = validated_data['phone_number'],
            )
            user.set_password(validated_data['password'])
            user.save()
        except:
            raise serializers.ValidationError({"error": "failed to create account"})
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        new_pass = validated_data.get('password', None)
        if new_pass:
            instance.set_password(new_pass)
        instance.save()
        return instance


class MainUserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number')
        read_only_fields = fields

        