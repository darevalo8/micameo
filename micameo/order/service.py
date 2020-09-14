from micameo.order.models import Order
from micameo.users.selectors import find_talent_by_username
from micameo.order.selectors import get_occasion


def create_order(**kwargs) -> Order:
    order = Order(
        email_client=kwargs['email_client'],
        talent=find_talent_by_username(kwargs['talent']),
        is_public=kwargs['is_public'],
        to=kwargs['to'],
        from_client=kwargs['from_client'],
        occasion=get_occasion(kwargs['occasion']),
        phone_number=kwargs['phone_number'],
        instructions=kwargs['instructions'],
        order_state=kwargs['order_state']

    )
    order.full_clean()
    order.save()
    return order
