from django.db import models
from model_utils.models import TimeStampedModel
from micameo.users.models import Talent
from micameo.order.models import Order


class BalanceOrder(TimeStampedModel):
    balance_name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0)

    def __str__(self):
        return self.balance_name


class BalanceOrderDetail(TimeStampedModel):
    balance = models.ForeignKey(BalanceOrder, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, models.CASCADE)

    def __str__(self):
        return str(self.balance)


class BalanceMiCameo(TimeStampedModel):
    balance_name = models.CharField(max_length=50, default='Micameo')
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0)

    def __str__(self):
        return self.balance_name


class BalanceTalent(TimeStampedModel):
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0)

    def __str__(self):
        return str(self.talent)


class BalanceTalentDetail(TimeStampedModel):
    balance = models.ForeignKey(BalanceTalent, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.balance)


class RePay(TimeStampedModel):
    TRANSACTION_CHOICES = (
        (1, 'PENDIENTE'),
        (2, 'PAGADA'),

    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    state_repay = models.IntegerField(choices=TRANSACTION_CHOICES, default=1)

    def __str__(self):
        return str(self.order)


class Withdraw(TimeStampedModel):
    TRANSACTION_CHOICES = (
        (1, 'PENDIENTE'),
        (2, 'PAGADA'),
        (3, 'RECHAZADA'),

    )
    balance_talent = models.ForeignKey(BalanceTalent, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    state_withdraw = models.IntegerField(choices=TRANSACTION_CHOICES, default=1)

    def __str__(self):
        return str(self.balance_talent)
