from rest_framework import serializers

from .models import Ingredients, IngredientsAmount


class IngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'name',
            'measurement_unit',
        )
        model = Ingredients


class IngredientsAmountSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        queryset=Ingredients.objects.all(),
    )
    name = serializers.CharField(source="ingredient.name")
    measurement_unit = serializers.CharField(
        source="ingredient.measurement_unit",
    )
    class Meta:
        fields = (
            'id',
            'name',
            'measurement_unit',
            'amount',
        )
        model = IngredientsAmount


class IngredientsAmountAddSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        source='ingredient',
        queryset=Ingredients.objects.all(),
    )
    class Meta:
        fields = (
            'id',
            'amount',
        )
        model = IngredientsAmount