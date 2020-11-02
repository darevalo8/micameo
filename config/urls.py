from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from micameo.users.api.views import TalentUpdateApi

urlpatterns = [
                  path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
                  path(
                      "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
                  ),
                  # Django Admin, use {% url 'admin:index' %}
                  path(settings.ADMIN_URL, admin.site.urls),
                  # User management
                  path("users/", include("micameo.users.urls", namespace="users")),
                  path("accounts/", include("allauth.urls")),
                  # path('auth/', include('rest_framework_social_oauth2.urls')),
                  # Your stuff: custom urls includes go here
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("api/auth/users/", include("micameo.users.urls", namespace="users_api")),
    #     ORDER URL
    path("api/orders/", include("micameo.order.urls", namespace="order_api")),
    path("api/talent/<str:username>/", view=TalentUpdateApi.as_view()),
    #    BALANCE URL
    path("api/balance/", include("micameo.balance.urls")),
    #    FAVORITE URL
    path("api/favorite/", include("micameo.favorites.urls")),

]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
