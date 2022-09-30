from django.db.models import F, Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ingredients.models import IngredientsAmount

from .filter import RecipeFilter
from .models import Favorite, Recipes, ShoppingCart
from .permissions import IsAuthorOrReadOnly
from .serializers import (RecipesCreateSerializer, RecipesReadSerializer,
                          ShortRecipeSerializer)


class RecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    permission_classes = (IsAuthorOrReadOnly, )
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RecipeFilter
    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return RecipesReadSerializer
        return RecipesCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def add(self, model, user, pk):
        """Добавление рецепта в списки"""
        recipe = get_object_or_404(Recipes, pk=pk)
        model.objects.create(user=user, recipe=recipe)
        serializer = ShortRecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete_relation(self, model, user, pk):
        """"Удаление рецепта из списков"""
        recipe = get_object_or_404(Recipes, pk=pk)
        relation = model.objects.filter(user=user, recipe=recipe)
        relation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        methods=['post', 'delete'],
        detail=True,
    )
    def favorite(self, request, pk=None):
        """Добавление и удаление Избранное."""
        user = request.user
        if request.method == 'POST':
            return self.add(Favorite, user, pk)
        if request.method == 'DELETE':
            return self.delete_relation(Favorite, user, pk)

    @action(
        methods=['post', 'delete'],
        detail=True,
    )
    def shopping_cart(self, request, pk=None):
        """Добавление и удаление в Список покупок."""
        user = request.user
        if request.method == 'POST':
            return self.add(ShoppingCart, user, pk)
        if request.method == 'DELETE':
            return self.delete_relation(ShoppingCart, user, pk)
    
    @action(
        methods=['get'],
        detail=False,
    )
    def download_shopping_cart(self, request):
        """Формирование и скачивание списка покупок."""
        shopping_list = IngredientsAmount.objects.filter(
            recipes__shoppingcart__user=request.user
        ).values(
            name=F('ingredient__name'),
            measurement_unit=F('ingredient__measurement_unit')
        ).annotate(amount=Sum('amount')).values_list(
            'ingredient__name', 'amount', 'ingredient__measurement_unit'
        )
        data = ''.join(f'{key} - {value} - {unit}\n' for key, value, unit in shopping_list)
        return HttpResponse(data, content_type='text/plain')
        