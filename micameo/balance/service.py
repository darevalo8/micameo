from micameo.balance.models import (BalanceTalent, BalanceOrderDetail, BalanceTalentDetail)
from micameo.balance.selectors import (get_balance_order, get_balance_talent, get_balance_micameo)
from micameo.users.models import Talent
from micameo.order.models import Order
import decimal


def create_balance_talent(talent: Talent) -> BalanceTalent:
    balance = BalanceTalent(talent=talent, amount=0)
    balance.full_clean()
    balance.save()
    return balance


def create_balance_detail(order: Order) -> BalanceOrderDetail:
    balance = BalanceOrderDetail(order=order, balance=get_balance_order())
    balance.full_clean()
    balance.save()
    return balance


def create_balance_talent_detail(order: Order) -> BalanceTalentDetail:
    balance = BalanceTalentDetail(order=order, balance=get_balance_talent(order.talent))
    balance.full_clean()
    balance.save()
    return balance


def add_amount_to_balance_order(order: Order):
    balance = get_balance_order()
    balance.amount += order.order_price
    balance.full_clean()
    balance.save()


def add_amount_to_talent_and_micameo(order: Order):
    balance_order = get_balance_order()
    balance_talent = get_balance_talent(order.talent)
    balance_micameo = get_balance_micameo()
    balance_talent.amount += decimal.Decimal((float(order.order_price) - (float(order.order_price) * 0.25)))
    balance_micameo.amount += decimal.Decimal((float(order.order_price) * 0.25))
    balance_order.amount -= order.order_price
    balance_order.full_clean()
    balance_talent.full_clean()
    balance_micameo.full_clean()
    balance_order.save()
    balance_talent.save()
    balance_micameo.save()
