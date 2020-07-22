from rest_framework import serializers
from micameo.users.models import Client

from .user_serializer import UserSerializer


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Client
        fields = ['user', 'profile_image', 'phone_number', 'birthday']
