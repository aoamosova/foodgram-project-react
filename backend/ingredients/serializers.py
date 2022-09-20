from cgitb import lookup
from dataclasses import fields
from rest_framework import serializers

from .models import Ingredients


class IngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Ingredients