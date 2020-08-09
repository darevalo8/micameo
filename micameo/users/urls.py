from django.urls import path

from micameo.users.api.views import (
    RegisterTalent,
    RegisterClient,
    activate,
    CustomTokenObtainPairView
)
from micameo.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("register-talent", RegisterTalent.as_view(), name="register_talent"),
    path("register-client", RegisterClient.as_view(), name="register_client"),
    path("activate/<slug:uidb64>/<slug:token>", view=activate, name="activate"),
    path("login", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
]
