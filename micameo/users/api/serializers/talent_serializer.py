from rest_framework import serializers
from micameo.users.models import Talent
from .user_serializer import UserSerializer


class TalentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    categories = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Talent
        fields = ['user', 'profile_image', 'description', 'response_days', "price", "url", "categories", "birthday"]

        extra_kwargs = {
            "url": {"view_name": "api:talent-detail", "lookup_field": "slug"}
        }
