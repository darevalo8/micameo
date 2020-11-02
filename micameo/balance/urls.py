from django.urls import path
from micameo.balance.api.views import GetBalanceTalentApi

app_name = "balance"
urlpatterns = [
    path("", view=GetBalanceTalentApi.as_view(), name="get_balance"),
]
