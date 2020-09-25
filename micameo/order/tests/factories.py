import factory.fuzzy
from factory import (django, )

from micameo.order.models import Order, Occasion, Cameo
from micameo.users.tests.factories import TalentFactory


class OccasionFactory(django.DjangoModelFactory):
    class Meta:
        model = Occasion


class OrderFactory(django.DjangoModelFactory):
    class Meta:
        model = Order

    occasion = factory.SubFactory(OccasionFactory)
    talent = factory.SubFactory(TalentFactory)


class CameoFactory(django.DjangoModelFactory):
    class Meta:
        model = Cameo

    order = factory.SubFactory(OrderFactory)
