from rest_framework import filters
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from micameo.users.api.serializers import TalentSerializer
from micameo.users.helpers import RegisterUser
from micameo.users.models import Talent


class TalentViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Talent.objects.all()
    serializer_class = TalentSerializer
    lookup_field = "slug"
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['slug', 'user__first_name', 'user__last_name', 'categories__sub_name']


class RegisterTalent(RegisterUser):
    model = Talent
