from micameo.order.models import Occasion, Order
from django.core.exceptions import ValidationError


def get_occasion(occasion_name: str) -> Occasion:
    try:
        occasion = Occasion.objects.get(occasion_name=occasion_name)
    except Occasion.DoesNotExist:
        raise ValidationError("Ocasion no existe")
    return occasion


def get_orders_by_client(email: str):
    try:
        orders = Order.objects.filter(email_client=email)
    except Order.DoesNotExist:
        orders = []

    return orders


def get_orders_by_talent(user):
    try:
        orders = Order.objects.filter(talent__user=user, order_state=2)
    except Order.DoesNotExist:
        orders = []

    return orders
