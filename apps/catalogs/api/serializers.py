from apps.abstracts.serializers import AbstractSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from apps.catalogs.models import State, City
import json


class StateSerializer(AbstractSerializer):
    state = serializers.CharField(read_only=True)

    def validate_state(self, value):
        if self.context["request"].pk != value:
            raise ValidationError
        return value

    class Meta:
        model = State
        fields = ["id", "state", "created", "updated", "is_active"]
        read_only_fields = ["created", "updated", "is_active"]


class CitySerializer(AbstractSerializer):
    city = serializers.CharField(read_only=True)
    state = serializers.CharField(read_only=True)

    def validate_city(self, value):
        print("VALUES: ", isinstance(value, json))
        if self.context["request"].city != value:
            raise ValidationError("State requiered doesn't match")
        return value

    class Meta:
        model = City
        fields = ["id", "city", "created", "updated", "is_active", "state"]
        read_only_fields = ["created", "updated", "is_active"]
