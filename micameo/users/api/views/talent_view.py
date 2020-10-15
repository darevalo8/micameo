from rest_framework import filters
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from micameo.users.api.serializers import TalentSerializer, TalentUpdateSerializer
from micameo.users.helpers import RegisterUser
from micameo.users.models import Talent


class TalentViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Talent.objects.all()
    serializer_class = TalentSerializer
    lookup_field = "slug"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['slug', 'user__first_name', 'user__last_name', 'categories__sub_name']

    @action(detail=False, methods=["GET"])
    def me(self, request):
        queryset = self.get_queryset()
        serializer = TalentSerializer(queryset.get(slug=request.user), context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class TalentUpdateViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin,
                          GenericViewSet):
    queryset = Talent.objects.all()
    serializer_class = TalentUpdateSerializer
    lookup_field = "slug"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RegisterTalent(RegisterUser):
    model = Talent
