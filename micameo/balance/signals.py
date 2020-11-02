from django.db.models.signals import post_save
from django.dispatch import receiver

from micameo.balance.selectors import (get_balance_talent, get_balance_detail_order,
                                       get_balance_detail_talent)
from micameo.balance.service import (create_balance_talent, create_balance_detail,
                                     add_amount_to_balance_order, create_balance_talent_detail,
                                     add_amount_to_talent_and_micameo)
from micameo.users.models import Talent
from micameo.order.models import Order


@receiver(post_save, sender=Talent)
def create_balance_for_new_talents(sender, instance, created, **kwargs):
    balance = get_balance_talent(instance)
    if not balance:
        create_balance_talent(instance)


@receiver(post_save, sender=Order)
def create_balance_for_new_talents(sender, instance, created, **kwargs):
    if instance.order_state == 1:
        balance_detail = get_balance_detail_order(instance)
        if not balance_detail:
            create_balance_detail(instance)
            add_amount_to_balance_order(instance)
    if instance.talent_response == 5:
        balance_talent = get_balance_detail_talent(instance)
        if not balance_talent:
            create_balance_talent_detail(instance)
            add_amount_to_talent_and_micameo(instance)



