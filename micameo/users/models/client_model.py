from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel
from .user_model import User


class Client(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message=_('Phone number must be entered in the format: +9999999. Up to 10-15 digits allowed')
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    birthday = models.DateField(_("Day of Birthday"))
