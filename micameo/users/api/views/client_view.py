from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from micameo.users.api.serializers import ClientSerializer
from micameo.users.helpers import RegisterUser
from micameo.users.models import Client


class RegisterClient(RegisterUser):
    model = Client


class ClientViewSet(ListModelMixin, UpdateModelMixin,
                    RetrieveModelMixin, GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = "slug"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=["GET"])
    def me(self, request):
        queryset = self.get_queryset()
        try:
            client_profile = queryset.get(slug=request.user)
        except Client.DoesNotExist:
            client_profile = Client.objects.create(user=request.user)
        serializer = ClientSerializer(client_profile, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)
