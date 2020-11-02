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
