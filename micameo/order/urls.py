from django.urls import path
from micameo.order.api.views import (CreateOrderApi, OrderListTalentApi,
                                     OrderListClientApi, CreateCameoApi)

app_name = "order"
urlpatterns = [
    path("", view=CreateOrderApi.as_view(), name="add_order"),
    path("<int:pk>/", view=CreateOrderApi.as_view(), name="update_order"),

    path("talent", view=OrderListTalentApi.as_view(), name="get_order_with_talent"),
    path("talent/<int:pk>/", view=OrderListTalentApi.as_view(), name="get_order_with_talent"),
    path("client", view=OrderListClientApi.as_view(), name="get_order_with_client"),
    path("cameo", view=CreateCameoApi.as_view(), name="add_cameo"),
    path("cameo/<int:pk>/", view=CreateCameoApi.as_view(), name="update_and_detail_cameo"),
]
