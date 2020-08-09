from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from micameo.users.models import Talent, Client
from micameo.users.models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.is_active = False
        user.save()
        return user

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password", "url"]
        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
            "password": {'write_only': True}
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
