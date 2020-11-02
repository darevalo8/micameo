from django.db.models.signals import post_save
from django.dispatch import receiver

from micameo.users.models import User, Talent, Client


@receiver(post_save, sender=User)
def change_slug_for_talent_client(sender, instance, created, **kwargs):
    try:
        talent = Talent.objects.get(user=instance)
    except Talent.DoesNotExist:
        talent = None
    try:
        client = Client.objects.get(user=instance)
    except Client.DoesNotExist:
        client = None
    if talent:
        talent.slug = instance.username
        talent.clean()
        talent.save()


    elif client:
        client.slug = instance.username
        client.clean()
        client.save()
