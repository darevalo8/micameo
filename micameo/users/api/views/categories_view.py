from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions
from ..serializers import CategorySerializer, SubCategorySerializer
from micameo.users.models import Category, SubCategory


class CategoryViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "name"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SubCategoryViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()
    lookup_field = "sub_name"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
