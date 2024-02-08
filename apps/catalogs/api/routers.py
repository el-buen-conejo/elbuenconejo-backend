from apps.catalogs.api.viewsets import StateViewSet, CityViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register(r"states", StateViewSet, basename="states")
routers.register(r"cities", CityViewSet, basename="cities")
urlpatterns = routers.urls
