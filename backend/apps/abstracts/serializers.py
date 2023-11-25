from rest_framework import serializers


class AbstractSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)

    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
