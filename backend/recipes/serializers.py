from cgitb import lookup
from dataclasses import fields
from rest_framework import serializers

from .models import Recipes


class RecipesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Recipes