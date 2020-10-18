from django.urls import path
from micameo.order.api.views import (CreateOrderApi, OrderListTalentApi,
                                     OrderListClientApi, OrderAcceptListTalentApi,
                                     CreateCameoApi, GetCameoClientApi, GetTotalOrdersPendingAndCompleteApi,
                                     GetOrdersPerMonthTalentApi, GetOrdersPerMonthClientApi,
                                     GetCameosPublicTalentApi, GetOrdersByOccasionApi,
                                     ListOccasionApi)

app_name = "order"
urlpatterns = [
    path("", view=CreateOrderApi.as_view(), name="add_order"),
    path("<int:pk>/", view=CreateOrderApi.as_view(), name="update_order"),
    path("talent", view=OrderListTalentApi.as_view(), name="get_order_with_talent"),
    path("talent/accept", view=OrderAcceptListTalentApi.as_view(), name="get_order_with_talent_accept"),
    path("talent/<int:pk>/", view=OrderListTalentApi.as_view(), name="get_order_with_talent_update"),
    path("client", view=OrderListClientApi.as_view(), name="get_order_with_client"),
    path("cameo", view=CreateCameoApi.as_view(), name="add_cameo"),
    path("cameo/client", view=GetCameoClientApi.as_view(), name="get_cameo_by_client"),
    path("cameo/talent", view=GetCameosPublicTalentApi.as_view(), name="get_cameo_public"),
    path("cameo/<int:pk>/", view=CreateCameoApi.as_view(), name="update_and_detail_cameo"),
    path("talent/pending/", view=GetTotalOrdersPendingAndCompleteApi.as_view(), name="get_orders_pending"),
    path("talent-occasion", view=GetOrdersByOccasionApi.as_view(), name="get_orders_by_occasion"),
    path("talent-per-month", view=GetOrdersPerMonthTalentApi.as_view(), name="get_orders_per_mont_talent"),
    path("client-per-month", view=GetOrdersPerMonthClientApi.as_view(), name="get_orders_per_mont_client"),
    path("occasion-list", view=ListOccasionApi.as_view(), name="occasion_list"),

]
