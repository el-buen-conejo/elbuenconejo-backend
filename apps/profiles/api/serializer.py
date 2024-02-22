from rest_framework import serializers
from apps.profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfilePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("photo",)

    def update(self, instance, validated_data):
        instance.photo = validated_data.get("photo", instance.photo)
        instance.save()
        return instance
