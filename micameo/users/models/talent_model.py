from django.db import models
from django.utils.translation import ugettext_lazy as _

from .user_model import BaseUser
from micameo.users.models import SubCategory


class Talent(BaseUser):
    description = models.TextField(_("Your Description"), max_length=600, blank=True)
    response_days = models.IntegerField(default=7)
    categories = models.ManyToManyField(
        SubCategory,
        related_name='talent_category',
        blank=True
    )
    # slug = models.SlugField(max_length=50, unique=True, blank=True)
    price = models.DecimalField(_("Price of cameo"), max_digits=19, decimal_places=2, default=10.0)

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     self.slug = self.user.username
    #     super(Talent, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return str(self.user)
