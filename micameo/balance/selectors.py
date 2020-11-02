from micameo.balance.models import (BalanceTalent, BalanceOrderDetail,
                                    BalanceOrder, BalanceTalentDetail, BalanceMiCameo)
from micameo.users.models import Talent


def get_balance_talent(talent: Talent) -> BalanceTalent:
    try:
        balance = BalanceTalent.objects.get(talent=talent)
    except BalanceTalent.DoesNotExist:
        balance = None
    return balance


def get_balance_detail_order(order) -> BalanceOrderDetail:
    try:
        balance = BalanceOrderDetail.objects.get(order=order)
    except BalanceOrderDetail.DoesNotExist:
        balance = None
    return balance


def get_balance_detail_talent(order) -> BalanceTalentDetail:
    try:
        balance = BalanceTalentDetail.objects.get(order=order)
    except BalanceTalentDetail.DoesNotExist:
        balance = None
    return balance


def get_balance_order() -> BalanceOrder:
    balance = BalanceOrder.objects.get(balance_name="General")
    return balance


def get_balance_micameo() -> BalanceMiCameo:
    balance = BalanceMiCameo.objects.get(balance_name="Micameo")
    return balance
