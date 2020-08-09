from rest_framework import serializers

from micameo.users.models import Talent
from .user_serializer import UserSerializer


class TalentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    categories = serializers.StringRelatedField(many=True, read_only=True)

    # def to_internal_value(self, data):
    #     print(data["user"]['username'])
    #     categories = []
    #     for category in data['categories']:
    #         print(category)
    #         try:
    #             category_object = SubCategory.objects.get(sub_name=category)
    #             categories.append(category_object)
    #         except SubCategory.DoesNotExist:
    #             pass
    #
    #     res = {
    #         "user": User.objects.get(username=data["user"]['username']),
    #         "profile_image": data['profile_image'],
    #         "description": data['description'],
    #         "response_days": data['response_days'],
    #         "price": data['price'],
    #         "categories": categories,
    #         "birthday": data['birthday']
    #     }
    #     return res

    class Meta:
        model = Talent
        fields = ['user', 'profile_image', 'description', 'response_days', "price", "url", "categories", "birthday"]
        # read_only_fields = ['user', ]
        extra_kwargs = {
            "url": {"view_name": "api:talent-detail", "lookup_field": "slug"},
            "user": {"required": False},

        }
        # depth = 1
