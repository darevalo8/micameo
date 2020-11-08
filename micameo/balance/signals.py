from django.db.models.signals import post_save
from django.dispatch import receiver

from micameo.balance.selectors import (get_balance_detail_order,
                                       get_balance_detail_talent)
from micameo.balance.service import (create_balance_detail,
                                     add_amount_to_balance_order, create_balance_talent_detail,
                                     add_amount_to_talent_and_micameo, add_repay)
from micameo.order.models import Order
from micameo.order.service import send_rejected_order_mail, send_cameo


@receiver(post_save, sender=Order)
def create_balance_for_new_talents(sender, instance, created, **kwargs):
    if instance.order_state == 1:
        balance_detail = get_balance_detail_order(instance)
        if not balance_detail:
            create_balance_detail(instance)
            add_amount_to_balance_order(instance)
    if instance.talent_response == 3:
        add_repay(instance)
        send_rejected_order_mail(instance)
    if instance.talent_response == 5:
        balance_talent = get_balance_detail_talent(instance)
        if not balance_talent:
            create_balance_talent_detail(instance)
            add_amount_to_talent_and_micameo(instance)
            send_cameo(instance)
