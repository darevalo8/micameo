from rest_framework import permissions
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from micameo.users.helpers import RegisterUser
from micameo.users.models import Client
from micameo.users.api.serializers import ClientSerializer


class RegisterClient(RegisterUser):
    model = Client


class ClientViewSet(ListModelMixin, UpdateModelMixin,
                    RetrieveModelMixin, GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = "slug"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
