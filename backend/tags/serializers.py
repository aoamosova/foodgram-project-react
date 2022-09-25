from rest_framework import serializers

from .models import Tags
from recipes.models import Recipes


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'color',
            'slug',
        )
        model = Tags
