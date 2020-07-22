from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import filters
from rest_framework import permissions
from ..serializers import TalentSerializer
from micameo.users.models import Talent
from ...helpers import RegisterUser


class TalentViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = TalentSerializer
    queryset = Talent.objects.all()
    lookup_field = "slug"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['slug', 'user__first_name', 'user__last_name', 'categories__sub_name']

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(id=self.request.user.id)

    # def list(self, request, *args, **kwargs):
    #
    #     serializer = TalentSerializer(self.queryset, context={"request": request}, many=True)
    #     return Response(status=status.HTTP_200_OK, data=serializer.data)


class RegisterTalent(RegisterUser):
    model = Talent
