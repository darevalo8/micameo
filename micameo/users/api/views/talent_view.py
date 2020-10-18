from rest_framework import filters
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from micameo.users.api.serializers import TalentSerializer, TalentUpdateSerializer
from micameo.users.helpers import RegisterUser
from micameo.users.models import Talent
from micameo.utils.utils import ApiErrorsMixin
from micameo.users.service import update_talent


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


# class TalentUpdateViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin,
#                           GenericViewSet):
#     queryset = Talent.objects.all()
#     serializer_class = TalentUpdateSerializer
#     lookup_field = "slug"
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TalentUpdateApi(ApiErrorsMixin, APIView):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def put(request, username):
        serializer = TalentUpdateSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        talent_response = update_talent(username=username, **serializer.validated_data)
        serializer_response = TalentSerializer(talent_response, context={"request": request})
        return Response(serializer_response.data, status=status.HTTP_200_OK)


class RegisterTalent(RegisterUser):
    model = Talent
