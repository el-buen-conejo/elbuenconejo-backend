from rest_framework import serializers
from ..models import Farm


class farmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = "__all__"


class FarmPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = ("photo",)

    def update(self, instance, validated_data):
        instance.photo = validated_data.get("photo", instance.photo)
        instance.save()
        return instance
