from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from micameo.users.api.views import (UserViewSet, CategoryViewSet,
                                     SubCategoryViewSet, TalentViewSet)

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("categories", CategoryViewSet)
router.register("sub-categories", SubCategoryViewSet)
router.register("talent", TalentViewSet)

app_name = "api"
for i in router.urls:
    print(i)
urlpatterns = router.urls
