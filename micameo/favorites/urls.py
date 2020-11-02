from django.urls import path
from micameo.favorites.api.views import FavoriteApi

app_name = "order"
urlpatterns = [
    path("", view=FavoriteApi.as_view(), name="list_favorites"),
    path("delete/<int:pk>", view=FavoriteApi.as_view(), name="delete_favorites"),
]
