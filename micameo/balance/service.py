import decimal

from django.template.loader import render_to_string

from micameo.balance.models import (BalanceTalent, BalanceOrderDetail, BalanceTalentDetail, RePay, Withdraw)
from micameo.balance.selectors import (get_balance_order, get_balance_talent, get_balance_micameo)
from micameo.order.models import Order
from micameo.users.models import Talent
from django.core.exceptions import ValidationError

from micameo.users.tasks import send_email_notification


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


def add_repay(order: Order) -> RePay:
    repay = RePay(order=order)
    repay.full_clean()
    repay.save()
    return repay


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


def add_withdraw(balance_talent: BalanceTalent, amount: str) -> Withdraw:
    amount_decimal = decimal.Decimal(amount)
    if amount_decimal == 0:
        raise ValidationError("El valor ingresado no es valido es 0")

    elif amount_decimal <= balance_talent.amount:
        withdraw = Withdraw(balance_talent=balance_talent, amount=amount_decimal)
        withdraw.full_clean()
        withdraw.save()
        message = render_to_string('notify_admins_template.html', {
            "withdraw": withdraw,
        })
        to_email = ['danielfelipe.arevalo2@gmail.com', "sergio6006@hotmail.com", "andresgiraldo99@hotmail.com"]
        send_email_notification("Retiro Talento {0}".format(withdraw.balance_talent.talent), message=message, to_email=to_email)
    else:
        raise ValidationError("El valor ingresado es mayor al valor que tiene en su cuenta")

    return withdraw
