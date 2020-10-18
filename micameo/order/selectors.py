from django.core.exceptions import ValidationError
from django.db.models import Count

from micameo.order.models import Occasion, Order, Cameo
from micameo.users.models import User


# OCCASIONS QUERIES
def get_occasion(occasion_name: str) -> Occasion:
    try:
        occasion = Occasion.objects.get(occasion_name=occasion_name)
    except Occasion.DoesNotExist:
        raise ValidationError("Ocasion no existe")
    return occasion


def list_occasion():
    return Occasion.objects.all()


# ORDERS QUERIES
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
    orders = Order.objects.filter(talent__user=user, order_state=1, talent_response=1)
    return orders


def get_orders_by_talent_accept(user: User) -> Order:
    orders = Order.objects.filter(talent__user=user, order_state=1, talent_response=2)
    return orders


def get_orders_pending_and_completed(user: User):
    pending_orders = Order.objects.filter(talent__user=user, order_state=1, talent_response=1).count()
    completed_orders = Order.objects.filter(talent__user=user, order_state=1, talent_response=5).count()

    data = {
        'ordenes_pendientes': pending_orders,
        'odenes_completadas': completed_orders
    }
    return data


def get_orders_per_month_talent(user: User, month: int):
    orders = Order.objects.filter(talent__user=user, talent_response=5, created__month=month)

    return orders


def get_orders_per_month_client(email: str, month: int):
    orders = Order.objects.filter(email_client=email, created__month=month)

    return orders


def get_orders_by_occasion_talent(user: User):
    order = Order.objects.values("occasion__occasion_name").annotate(total_order=Count("occasion")).filter(
        talent__user=user, talent_response=5)

    return order


# CAMEOS QUERIES
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


def get_cameo_public_by_talent(user: str):
    return Cameo.objects.filter(order__talent__slug=user, order__is_public=True)
