from django.urls import path
from micameo.balance.api.views import GetBalanceTalentApi, WithdrawApi

app_name = "balance"
urlpatterns = [
    path("", view=GetBalanceTalentApi.as_view(), name="get_balance"),
    path("withdraw", view=WithdrawApi.as_view(), name="withdraw"),

]
