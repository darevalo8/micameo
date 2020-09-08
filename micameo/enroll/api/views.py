from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from micameo.enroll.api.serializers import EnrollSerializer
from micameo.enroll.models import Enroll


class EnrollViewSet(ListModelMixin, RetrieveModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer
