from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions
from ..serializers import TalentSerializer
from micameo.users.models import Talent


class TalentViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = TalentSerializer
    queryset = Talent.objects.all()
    lookup_field = "name"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
