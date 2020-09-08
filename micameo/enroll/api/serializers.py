from rest_framework import serializers
from micameo.enroll.models import Enroll


class EnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enroll
        fields = ["full_name", "email", "phone_number", "where_find_you", "username", "followers"]
