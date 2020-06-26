from rest_framework import serializers

from micameo.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]

        # extra_kwargs = {
        #     "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        # }
