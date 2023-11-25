from apps.catalogs.models import State, City
from .serializers import StateSerializer, CitySerializer
from apps.abstracts.viewsets import AbstractViewSet
from utils.mixin_classes.mixin_class import CommonViewSetMixin


class StateViewSet(CommonViewSetMixin, AbstractViewSet):
    serializer_class = StateSerializer

    def get_queryset(self):
        return State.objects.all()

    def get_object(self):
        obj = State.object_state.get_object_state_by_id(self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj


class CityViewSet(CommonViewSetMixin, AbstractViewSet):
    serializer_class = CitySerializer

    def get_queryset(self):
        return City.objects.all()

    def get_object(self):
        obj = City.object_city.get_object_by_city_id(self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
