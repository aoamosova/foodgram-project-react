import base64

from django.core.files.base import ContentFile
from rest_framework import serializers

from ingredients.models import IngredientsAmount
from ingredients.serializers import (IngredientsAmountAddSerializer,
                                     IngredientsAmountSerializer)
from tags.models import Tags
from tags.serializers import TagsSerializer
from users.serializers import CustomUserSerializer

from .models import Favorite, Recipes, ShoppingCart


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name=f'temp.{ext}')
        return super().to_internal_value(data)


class RecipesReadSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(read_only=True, many=True)
    author = CustomUserSerializer(required=False)
    ingredients = IngredientsAmountSerializer(many=True, required=False)
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

    def get_is_favorited(self, obj):
        """Статус - в избранном или нет."""
        return self._extracted_get(Favorite, obj)

    def get_is_in_shopping_cart(self, obj):
        """Статус - списке покупок или нет."""
        return self._extracted_get(ShoppingCart, obj)

    def _extracted_get(self, model, obj):
        request = self.context.get('request')
        return(
            request.user.is_authenticated
            and model.objects.filter(
                user=request.user, 
                recipe__id=obj.id).exists()
        )


class RecipesCreateSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tags.objects.all(),
        many=True,
        required=True,
    )
    ingredients = IngredientsAmountAddSerializer(many=True, required=False)
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
        """Добавление тегов и ингидинетов"""
        recipes.tags.set(tags_data)
        ingredient_amounts = []
        for item in ingredients_data:
            ingredient = item.get('ingredient')
            amount = item.get('amount')
            ingredient_amount, _ = IngredientsAmount.objects.get_or_create(
                ingredient=ingredient,
                amount=amount,
            )
            ingredient_amounts.append(ingredient_amount)
        recipes.ingredients.set(ingredient_amounts)
        return recipes
    
    def create(self, validated_data):
        """Создание рецепта"""
        tags_data = validated_data.pop('tags')
        ingredients_data = validated_data.pop('ingredients')
        recipes = Recipes.objects.create(**validated_data)
        return self.add_tags_and_ingredients(
            recipes, tags_data, ingredients_data
        )

    def update(self, instance, validated_data):
        """Редактирование рецепта"""
        instance.ingredients.clear()
        instance.tags.clear()
        tags_data = validated_data.pop("tags")
        ingredients_data = validated_data.pop("ingredients")
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return self.add_tags_and_ingredients(
            instance, tags_data, ingredients_data
        )


class ShortRecipeSerializer(serializers.ModelSerializer):
    image = Base64ImageField(
        max_length=None,
        use_url=True,
    )

    class Meta:
        model = Recipes
        fields = (
            "id",
            "name",
            "image",
            "cooking_time",
        )
