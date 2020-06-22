from rest_framework import serializers
from micameo.users.models import Talent


class TalentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    # categories = serializers.StringRelatedField()

    class Meta:
        model = Talent
        fields = ['user', 'profile_image', 'description', 'response_days']
