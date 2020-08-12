from rest_framework import serializers

from micameo.users.models import Talent
from .user_serializer import UserSerializer


class TalentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    categories = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Talent
        fields = ['user', 'profile_image', 'description', 'response_days', "price", "url", "categories", "birthday"]
        # read_only_fields = ['user', ]
        extra_kwargs = {
            "url": {"view_name": "api:talent-detail", "lookup_field": "slug"},
            "user": {"required": False},

        }
