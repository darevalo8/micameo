from rest_framework import serializers
from micameo.users.models import Talent

from .user_serializer import UserSerializer


class TalentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Talent
        fields = ['user', 'profile_image', 'description', 'response_days', "url"]

        extra_kwargs = {
            "url": {"view_name": "api:talent-detail", "lookup_field": "slug"}
        }
