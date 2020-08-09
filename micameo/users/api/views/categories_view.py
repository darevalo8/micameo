from rest_framework import permissions, filters
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from micameo.users.api.serializers import CategorySerializer, SubCategoryCustomSerializer, SubCategorySerializer
from micameo.users.models import Category, SubCategory


class CategoryViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin,
                      CreateModelMixin, GenericViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "name"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SubCategoryViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = SubCategoryCustomSerializer
    queryset = SubCategory.objects.all()
    lookup_field = "sub_name"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SubCategoryAddViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()
    filter_backends = [filters.SearchFilter]
    lookup_field = "sub_name"
    search_fields = ['sub_name', 'category__name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
