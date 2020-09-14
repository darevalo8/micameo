from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from micameo.users.models import Talent


class Occasion(TimeStampedModel):
    occasion_name = models.CharField(max_length=50)

    def __str__(self):
        return self.occasion_name


class Order(TimeStampedModel):
    TRANSACTION_CHOICES = (
        (1, 'PENDIENTE'),
        (2, 'APROBADO'),
        (3, 'RECHAZADO'),
        (4, 'DEVOLUCION')
    )
    PAY_CHOICES = (
        (1, 'PAYCO'),
        (2, 'TC'),
    )
    TALENT_CHOICE = (
        (1, 'PENDIENTE'),
        (2, 'ACEPTADO'),
        (3, 'RECHAZADO'),
        (4, 'EN PROCESO'),
        (5, 'FINALIZADO')
    )
    email_client = models.EmailField()
    order_state = models.IntegerField(choices=TRANSACTION_CHOICES, default=1)
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE)
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message=_('Phone number must be entered in the format: +9999999. Up to 10-15 digits allowed')
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    is_public = models.BooleanField(default=False)
    to = models.CharField(max_length=50)
    from_client = models.CharField(max_length=50, blank=True)
    occasion = models.ForeignKey(Occasion, on_delete=models.CASCADE)
    instructions = models.TextField(max_length=300)
    pay_method = models.IntegerField(choices=PAY_CHOICES, default=1)
    talent_response = models.IntegerField(choices=TALENT_CHOICE, default=1)

    def __str__(self):
        return self.email_client


class Cameo(TimeStampedModel):
    url_video = models.URLField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.order)
