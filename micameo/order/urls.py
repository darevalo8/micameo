from django.urls import path
from micameo.order.api.views import CreateOrderApi, OrderListTalentApi, OrderListClientApi

app_name = "order"
urlpatterns = [
    path("", view=CreateOrderApi.as_view(), name="add_order"),
    path("talent", view=OrderListTalentApi.as_view(), name="get_order_with_talent"),
    path("client", view=OrderListClientApi.as_view(), name="get_order_with_client"),
]
