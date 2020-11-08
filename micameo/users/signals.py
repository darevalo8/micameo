from django.db.models.signals import post_save
from django.dispatch import receiver

from micameo.balance.service import (create_balance_talent)
from micameo.users.models import Talent


@receiver(post_save, sender=Talent)
def create_balance_for_new_talents(sender, instance, created, **kwargs):
    print("Inicio signal")
    if created:
        create_balance_talent(instance)
