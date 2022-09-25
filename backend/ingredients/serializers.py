from rest_framework import serializers

from .models import Ingredients, IngredientsVolume


class IngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'name',
            'measurement_unit',
        )
        model = Ingredients


class IngredientsVolumeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='ingredients.id')
    name = serializers.ReadOnlyField(source='ingredients.name')
    measurement_unit = serializers.ReadOnlyField(
        source='ingredient.measurement_unit')
    volume = serializers.ReadOnlyField(
        source='ingredient.volume')
    class Meta:
        fields = (
            'id',
            'name',
            'measurement_unit',
            'volume',
        )
        model = IngredientsVolume


class IngredientsVolumeAddSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        source='ingridiens',
        queryset=Ingredients.objects.all(),
    )
    class Meta:
        fields = [
            'id',
            'volume',
        ]
        model = IngredientsVolume