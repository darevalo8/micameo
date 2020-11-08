from django.template.loader import render_to_string

from micameo.order.models import Order, Cameo
from micameo.order.selectors import get_occasion, get_order, get_cameo, get_cameo_by_order
from micameo.users.selectors import find_talent_by_username
from micameo.users.tasks import send_email_notification


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
        order_state=kwargs['order_state'],
        order_price=kwargs['order_price']

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


def send_cameo(order: Order):
    to_email = [order.email_client]
    cameo = get_cameo_by_order(order_id=order.id)
    message = render_to_string('cameo_template_email.html', {
        "cameo": cameo,
    })
    send_email_notification("Video Micameo", message=message, to_email=to_email)


def send_rejected_order_mail(order: Order):
    to_email = [order.email_client]
    message = render_to_string('cameo_rejected_template_email.html', {
        "order": order,
    })
    send_email_notification("Rembolso Cameo - Cameo Rechazado", message=message, to_email=to_email)
    # Notification to admins
    message = render_to_string('notify_admins_template.html', {
        "order": order,
    })
    to_email = ['danielfelipe.arevalo2@gmail.com', "sergio6006@hotmail.com", "andresgiraldo99@hotmail.com"]
    send_email_notification("Rembolso Orden", message=message, to_email=to_email)
