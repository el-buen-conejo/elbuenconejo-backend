from rest_framework.routers import DefaultRouter
from .viewsets import CageViewSet

router = DefaultRouter()
router.register(r'cages', CageViewSet, basename='cages')
urlpatterns = router.urls