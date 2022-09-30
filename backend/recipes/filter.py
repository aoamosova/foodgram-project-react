from django_filters import ModelMultipleChoiceFilter
from django_filters.rest_framework import FilterSet, filters

from recipes.models import Recipes
from tags.models import Tags
from users.models import User


class RecipeFilter(FilterSet):
    tags = ModelMultipleChoiceFilter(
        field_name='tags__slug',
        to_field_name='slug',
        queryset=Tags.objects.all()
    )
    author = filters.ModelChoiceFilter(queryset=User.objects.all())
    is_favorited = filters.BooleanFilter(method='filter_favorited')
    is_in_shopping_cart = filters.BooleanFilter(method='filter_shopping_cart')

    class Meta:
        model = Recipes
        fields = ('tags', 'author')
        
    def filter_favorited(self, queryset, name, value):
        return queryset.filter(favorite__user=self.request.user) if value else queryset

    def filter_shopping_cart(self, queryset, name, value):
        return queryset.filter(shoppingcart__user=self.request.user) if value else queryset
   