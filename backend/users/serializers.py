from djoser.serializers import UserSerializer
from rest_framework import serializers

from recipes.models import Recipes

from .models import Subscriptions, User


class CustomUserSerializer(UserSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        fields = (
           'email',
           'id',
           'username',
           'first_name',
           'last_name',
           'is_subscribed',
           'password',
        )
        model = User
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_is_subscribed(self, obj: User):
        """Статус подписки"""
        user = self.context['request'].user
        return (
            user.is_authenticated
            and Subscriptions.objects.filter(
            user=user, author=obj).exists()
        )

    def create(self, validated_data):
        """Создание нового пользователя."""
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = (
            "id",
            "name",
            "image",
            "cooking_time",
        )


class SubscriptionSerializer(UserSerializer):
    is_subscribed = serializers.SerializerMethodField()
    recipes = serializers.SerializerMethodField()
    recipes_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "email",
            "id",
            "username",
            "first_name",
            "last_name",
            "is_subscribed",
            "recipes",
            "recipes_count",
        )

    def get_recipes(self, obj):
        recipes = obj.recipes.all()[:3]
        request = self.context.get('request')
        return RecipesSerializer(
            recipes, many=True,
            context={'request': request}
        ).data

    def get_is_subscribed(self, obj: User):
        """Статус подписки"""
        user = self.context['request'].user
        return (
            user.is_authenticated
            and Subscriptions.objects.filter(
            user=user, author=obj).exists()
        )

    def get_recipes_count(self, obj):
        """Счетчик рецептов"""
        return Recipes.objects.filter(author=obj).count()
