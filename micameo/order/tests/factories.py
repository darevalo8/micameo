from factory import (django, )

from micameo.order.models import Order, Occasion


class OrderFactory(django.DjangoModelFactory):
    class Meta:
        model = Order


class OccasionFactory(django.DjangoModelFactory):
    class Meta:
        model = Occasion

