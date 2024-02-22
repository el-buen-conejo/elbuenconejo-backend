from apps.rabbits.api.viewsets import RabbitViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register(r"rabbits", RabbitViewSet, basename="rabbits")
urlpatterns = routers.urls
