from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework import filters
from rest_framework import permissions
from ..serializers import TalentSerializer
from micameo.users.models import Talent


class TalentViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = TalentSerializer
    queryset = Talent.objects.all()
    lookup_field = "slug"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['slug', 'user__first_name', 'user__last_name', 'categories__sub_name']

    # def list(self, request, *args, **kwargs):
    #
    #     serializer = TalentSerializer(self.queryset, context={"request": request}, many=True)
    #     return Response(status=status.HTTP_200_OK, data=serializer.data)
