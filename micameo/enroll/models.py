from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


# Create your models here.
class Enroll(TimeStampedModel):
    CHOICES = (
        (1, 'Facebook'),
        (2, 'Instagram'),
        (3, 'Twitter'),
        (4, 'YouTube'),
        (5, 'TikTok'),
        (6, 'Twitch'),
        (7, 'Otro'),
    )
    full_name = models.CharField(max_length=50, )
    email = models.EmailField(
        _('Email Address'),
        unique=True,
        error_messages={
            'unique': _('A user with that email already exist')
        }
    )
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message=_('Phone number must be entered in the format: +9999999. Up to 10-15 digits allowed')
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    where_find_you = models.IntegerField(choices=CHOICES, default=1)
    username = models.CharField(max_length=15)
    followers = models.IntegerField()

    def __str__(self):
        return self.full_name
