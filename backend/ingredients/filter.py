
from django.db.models import IntegerField, Value
from django_filters.rest_framework import FilterSet, filters

from .models import Ingredients


class IngredientSearchFilter(FilterSet):
    name = filters.CharFilter(method="search_by_name")

    class Meta:
        model = Ingredients
        fields = ("name",)

    def search_by_name(self, queryset, name, value):
        if not value:
            return queryset
        start_with_queryset = queryset.filter(
            name__istartswith=value
        ).annotate(order=Value(0, IntegerField()))
        contain_queryset = (
            queryset.filter(name__icontains=value)
            .exclude(
                pk__in=(ingredient.pk for ingredient in start_with_queryset)
            )
            .annotate(order=Value(1, IntegerField()))
        )
        return start_with_queryset.union(contain_queryset).order_by("order")