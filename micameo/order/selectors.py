from micameo.order.models import Occasion, Order, Cameo
from micameo.users.models import User
from django.core.exceptions import ValidationError


def get_occasion(occasion_name: str) -> Occasion:
    try:
        occasion = Occasion.objects.get(occasion_name=occasion_name)
    except Occasion.DoesNotExist:
        raise ValidationError("Ocasion no existe")
    return occasion


def list_occasion():
    return Occasion.objects.all()


def get_order(order_id) -> Order:
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        raise ValidationError("Order does no exist")
    return order


def get_orders_by_client(email: str) -> Order:
    orders = Order.objects.filter(email_client=email)

    return orders


def get_orders_by_talent(user: User) -> Order:
    orders = Order.objects.filter(talent__user=user, order_state=2, talent_response=1)
    return orders


def get_orders_by_talent_accept(user: User) -> Order:
    orders = Order.objects.filter(talent__user=user, order_state=2, talent_response=2)
    return orders


def get_cameo(cameo_id) -> Cameo:
    try:
        cameo = Cameo.objects.get(pk=cameo_id)
    except Cameo.DoesNotExist:
        raise ValidationError("Cameo does no exist")

    return cameo


def get_cameo_by_order(order_id) -> Cameo:
    try:
        cameo = Cameo.objects.get(order_id=order_id)
    except Cameo.DoesNotExist:
        raise ValidationError("Cameo does no exist")

    return cameo


def get_cameo_by_client(email: str) -> Cameo:
    return Cameo.objects.filter(order__email_client=email)
