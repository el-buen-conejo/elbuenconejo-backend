from rest_framework.routers import DefaultRouter
from apps.profiles.api.viewsets import ProfileModelViewSet

routers = DefaultRouter()
routers.register(r"profiles", ProfileModelViewSet, basename="profile")
urlpatterns = routers.urls
