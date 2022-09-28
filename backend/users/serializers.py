from cgitb import lookup
from dataclasses import fields

from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

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
        request = self.context.get('request')
        if not request or request.user.is_anonymous:
            return False
        return Subscriptions.objects.filter(
            user=user, author=obj).exists()

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
