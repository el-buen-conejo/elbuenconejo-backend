from apps.farms.api.viewsets import FarmViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"farms", FarmViewset, basename="farms")
urlpatterns = router.urls
