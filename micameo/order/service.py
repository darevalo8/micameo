from micameo.order.models import Order, Cameo
from micameo.users.selectors import find_talent_by_username
from micameo.order.selectors import get_occasion, get_order, get_cameo


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


def update_order_state(pk, order_state) -> Order:
    order = get_order(pk)
    order.order_state = int(order_state)
    order.save()
    return order


def update_order_talent_response(pk, order_response) -> Order:
    order = get_order(pk)
    order.talent_response = int(order_response)
    order.save()
    return order


# CAMEOS

def create_cameo(**kwargs) -> Cameo:
    cameo = Cameo(url_video=kwargs['url_video'],
                  order=get_order(kwargs['order'])
                  )
    cameo.full_clean()
    cameo.save()
    return cameo


def update_cameo(pk, url_video) -> Cameo:
    cameo = get_cameo(pk)
    cameo.url_video = url_video
    cameo.save()
    return cameo
