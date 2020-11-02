from django.contrib import admin
from micameo.order.models import (Order, Occasion, Cameo)


# Register your models here.
@admin.register(Occasion)
class Occasion(admin.ModelAdmin):
    list_display = ["occasion_name"]
    search_fields = ["occasion_name"]


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ["email_client", "order_state", "talent", "talent_response", "order_price", "created"]
    search_fields = ["email_client"]


@admin.register(Cameo)
class Cameo(admin.ModelAdmin):
    list_display = ["order", "url_video"]
    search_fields = ["order"]
