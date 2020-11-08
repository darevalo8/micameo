from django.contrib import admin
from micameo.balance.models import (BalanceOrder, BalanceTalent, BalanceMiCameo,
                                    BalanceTalentDetail, BalanceOrderDetail, RePay, Withdraw)


@admin.register(BalanceOrder)
class BalanceOrderAdmin(admin.ModelAdmin):
    list_display = ["balance_name", "amount"]


@admin.register(BalanceMiCameo)
class BalanceMicameoAdmin(admin.ModelAdmin):
    list_display = ["balance_name", "amount"]


@admin.register(BalanceTalent)
class BalanceTalentAdmin(admin.ModelAdmin):
    list_display = ["talent", "amount"]
    search_fields = ["talent"]


@admin.register(BalanceOrderDetail)
class BalanceOrderDetailAdmin(admin.ModelAdmin):
    list_display = ["balance", "order"]
    search_fields = ["balance"]


@admin.register(BalanceTalentDetail)
class BalanceTalentDetailAdmin(admin.ModelAdmin):
    list_display = ["balance", "order"]
    search_fields = ["balance"]


@admin.register(RePay)
class RePayAdmin(admin.ModelAdmin):
    list_display = ["order", "state_repay"]
    search_fields = ["order", ]


@admin.register(Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    list_display = ["balance_talent", "amount", "state_withdraw"]
    search_fields = ["balance_talent", ]
