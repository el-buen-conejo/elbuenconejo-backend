from rest_framework import serializers
from apps.cages.models import Cage
from apps.rabbits.api.serializers import RabbitSerializer


class CageSerializer(serializers.ModelSerializer):
    rabbits = serializers.SerializerMethodField()
    class Meta:
        model = Cage
        fields = "id", "created", "updated", "is_active", "count_rabbits", "price", "is_public", "total_weight", "photo", "farm_id",  "rabbits",
        read_only_fields = ( "id", "price", "count_rabbits", "total_weight", "created", "rabbits",)
        
    def get_rabbits(self, obj):
        rabbits = obj.rabbits.filter(is_active=True).order_by("-created",)
        return RabbitSerializer(rabbits, many=True).data
        


class CagePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cage
        fields = ("photo",)

    def update(self, instance, validated_data):
        instance.photo = validated_data.get("photo", instance.photo)
        instance.save()
        return instance
