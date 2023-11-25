from datetime import date
from rest_framework import serializers
from apps.rabbits.models import Rabbit
from dateutil.relativedelta import relativedelta

class RabbitSerializer(serializers.ModelSerializer):
    tag = serializers.CharField(required=True) 
    age = serializers.SerializerMethodField()

    class Meta:
        model = Rabbit
        fields = "__all__"
        # Cant update or eliminate
        read_only_fields = (
            "created",
            "id",
            "age",
            "tag",
        )
        
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("El precio no puede ser inferior a 0")
        if value > 5000:
            raise serializers.ValidationError("El precio no puede ser superior a 5000")
        return value

    def validate_birthday(self, value):
        today = date.today()
        delta = relativedelta(today, value)
        if value > today:
            raise serializers.ValidationError(
                f"El nacimiento no puede ser mayor que la fecha actual: {today}"
            )
        if delta.years > 10:
            raise serializers.ValidationError(
                "La edad del conejo no puede superar los 10 años."
            )
        return value

    def get_age(self, rabbit):
        today = date.today()
        delta = relativedelta(today, rabbit.birthday)
        age = f"{delta.years} años, {delta.months} meses y {delta.days} dias"
        return age

    def validate_weight(self, value):
        if value <= 0.0:
            raise serializers.ValidationError(
                f"El peso del conejo: {value} kg, tiene que ser mayor a 0 kg"
            )
        if value > 12.0:
            raise serializers.ValidationError(
                f"El peso del conejo: {value} kg, no puede ser mayor a 12 kg"
            )
        return value

    def create(self, validated_data):
        cage = validated_data.get("cage_id")
        rabbit = Rabbit.objects.create(**validated_data)

        if rabbit.is_active:
            cage.count_rabbits += 1
            cage.price += rabbit.price
            cage.total_weight += rabbit.weight
            cage.save()
        return rabbit

    def update(self, instance, validated_data):
        cage = instance.cage_id

        if instance.is_active:
            cage.price -= instance.price
            cage.total_weight -= instance.weight

        instance.breed = validated_data.get("breed", instance.breed)
        instance.genre = validated_data.get("genre", instance.genre)
        instance.birthday = validated_data.get("birthday", instance.birthday)
        instance.price = validated_data.get("price", instance.price)
        instance.tag = validated_data.get("tag", instance.tag)
        instance.weight = validated_data.get("weight", instance.weight)
        instance.photo = validated_data.get("photo", instance.photo)
        instance.save()
        
        if instance.is_active:
            cage.price += instance.price
            cage.total_weight += instance.weight
            cage.save()
        return instance
    
    def delete(self, instance):
        cage = instance.cage_id

        if instance.is_active:
            cage.count_rabbits -= 1
            cage.price -= instance.price
            cage.total_weight -= instance.weight
            cage.save()
    
        instance.is_active = False
        instance.save()



class RabbitPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rabbit
        fields = ("photo",)

    def update(self, instance, validated_data):
        instance.photo = validated_data.get("photo", instance.photo)
        instance.save()
        return instance
