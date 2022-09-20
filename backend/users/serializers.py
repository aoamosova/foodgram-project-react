from cgitb import lookup
from dataclasses import fields
from rest_framework import serializers
from djoser.serializers import UserSerializer, UserCreateSerializer

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
        )
        model = User

    def get_is_subscribed(self, obj):
        """Статус подписки"""
        user = self.context['request'].user
        return Subscriptions.objects.filter(
            user=user, author=obj).exists()


