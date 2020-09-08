from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from micameo.users.api.views import (UserViewSet, CategoryViewSet,
                                     SubCategoryViewSet, TalentViewSet,
                                     TalentUpdateViewSet, SubCategoryAddViewSet,
                                     ClientViewSet)
from micameo.enroll.api.views import EnrollViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("talents", TalentViewSet)
router.register("talent", TalentUpdateViewSet)
router.register("client", ClientViewSet)
router.register("categories", CategoryViewSet)
router.register("sub-category", SubCategoryAddViewSet)
router.register("sub-categories", SubCategoryViewSet)
router.register("enroll", EnrollViewSet)

app_name = "api"
for i in router.urls:
    print(i)
urlpatterns = router.urls
