from rest_framework import serializers
import base64
from django.core.files.base import ContentFile

from .models import Recipes, Favourites, ShoppingCart
from tags.models import Tags
from ingredients.models import IngredientsVolume
from users.serializers import CustomUserSerializer
from tags.serializers import TagsSerializer
from ingredients.serializers import (IngredientsVolumeSerializer,
                                    IngredientsVolumeAddSerializer)


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name=f'temp.{ext}')
        return super().to_internal_value(data)


class RecipesReadSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(read_only=True, many=True)
    author = CustomUserSerializer(read_only=True)
    ingredients = IngredientsVolumeSerializer(read_only=True, required=False)
    image = Base64ImageField()
    is_favorited = serializers.SerializerMethodField()
    is_in_shopping_cart = serializers.SerializerMethodField()
    class Meta:
        fields = (
            'id',
            'tags',
            'author',
            'ingredients',
            'is_favorited',
            'is_in_shopping_cart',
            'name',
            'image',
            'text',
            'cooking_time',
        )
        model = Recipes

    def _get_is_object_exists(self, model, obj):
        user = self.context["request"].user
        return (
            user.is_authenticated
            and model.objects.filter(
                user=user,
                recipe=obj,
            ).exists()
        )

    def get_is_favorited(self, obj):
        user = self.context['request'].user
        return Favourites.objects.filter(
            user=user, recipe=obj).exists()

    def get_is_in_shopping_cart(self, obj):
        user = self.context['request'].user
        return ShoppingCart.objects.filter(
            user=user, recipe=obj).exists()


class RecipesCreateSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tags.objects.all(),
        many=True,
        required=True,
    )
    ingredients = IngredientsVolumeAddSerializer(many=True)
    image = Base64ImageField()
    
    class Meta:
        fields = (
            'tags',
            'ingredients',
            'name',
            'image',
            'text',
            'cooking_time',
        ) 
        model= Recipes

    def add_tags_and_ingredients(self, recipes, tags_data, ingredients_data):
        recipes.tags.set(tags_data)
        for item in ingredients_data:
            ingredient = item.get('ingredient')
            volume = item.get('volume')
            ingredient_volume = IngredientsVolume.objects.get_or_create(
                ingredient=ingredient,
                volume=volume,
            )
            ingredient_volumes = [ingredient_volume]
        recipes.ingredients.set(ingredient_volumes)  
        return recipes
    
    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipes.objects.create(**validated_data)
        return self.add_tags_and_ingredients(
            recipe, tags_data, ingredients_data
        )
        

    # def update():