from rest_framework import serializers

from .user_serializer import UserSerializer
from micameo.users.models import Client


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Client
        fields = ['user', 'profile_image', 'phone_number', 'birthday', "url"]
        extra_kwargs = {
            "url": {"view_name": "api:client-detail", "lookup_field": "slug"},
            "user": {"required": False},

        }
