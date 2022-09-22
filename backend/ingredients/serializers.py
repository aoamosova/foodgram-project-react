from cgitb import lookup
from dataclasses import fields
from rest_framework import serializers

from .models import Ingredients, IngredientsVolume


class IngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Ingredients


class IngredientsVolumeSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        queryset = Ingredients.objects.all(),
    )
    name = serializers.CharField(
        source='ingredients.name',
    )
    measurment_unit = serializers.CharField(
        source='measurement_unit',
    ) 
    class Meta:
        fields = '__all__'
        model = IngredientsVolume