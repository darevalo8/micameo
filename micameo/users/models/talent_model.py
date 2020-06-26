from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel
from .user_model import User
from .category_model import SubCategory


class Talent(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.URLField(_("Your profile photo"), blank=True)
    description = models.TextField(_("Your Description"), max_length=600, blank=True)
    response_days = models.IntegerField(default=7)
    categories = models.ManyToManyField(
        SubCategory,
        related_name='talent_category',
        blank=True
    )
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = self.user.username
        super(Talent, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return str(self.user)
