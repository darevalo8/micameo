from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
# from rest_framework.response import Response
# from rest_framework import status
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

    # def list(self, request, *args, **kwargs):
    #
    #     serializer = SubCategorySerializer(self.queryset, context={"request": request}, many=True)
    #     return Response(status=status.HTTP_200_OK, data=serializer.data)
