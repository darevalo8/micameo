from rest_framework import serializers
from micameo.users.models import Category, SubCategory
from .talent_serializer import TalentSerializer


class SubCategorySerializer(serializers.ModelSerializer):
    talent_category = serializers.SerializerMethodField("get_talents_from_category")
    # talent_category = TalentSerializer(many=True, read_only=True)

    category = serializers.StringRelatedField()

    class Meta:
        model = SubCategory
        fields = ['sub_name', 'category', 'talent_category']

    def get_talents_from_category(self, obj):
        talents = obj.talent_category.all()[:6]
        talents_json = TalentSerializer(talents, many=True, context={"request": self.context['request']})
        return talents_json.data


class CategorySerializer(serializers.ModelSerializer):
    categorys = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'categorys', 'url']
        extra_kwargs = {
            "url": {"view_name": "api:category-detail", "lookup_field": "name"}
        }
