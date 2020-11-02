from django.contrib import admin
from micameo.balance.models import (BalanceOrder, BalanceTalent, BalanceMiCameo,
                                    BalanceTalentDetail, BalanceOrderDetail)


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
