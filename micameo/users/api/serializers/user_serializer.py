from rest_framework import serializers

from micameo.users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from ...models import Talent, Client


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]
        extra_kwargs = {
            # "url": {"view_name": "api:user-detail", "lookup_field": "username"},
            'password': {'write_only': True}
        }


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    This Custom serializer is created to know  who is logging talent or client on to the platform.
    """

    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        try:
            client_profile = Client.objects.get(user=self.user)
        except Client.DoesNotExist:
            client_profile = None

        try:
            talent_profile = Talent.objects.get(user=self.user)
        except Talent.DoesNotExist:
            talent_profile = None

        if client_profile:
            data.update({'is_talent': False})
        elif talent_profile:
            data.update({'is_talent': True})

        return data
