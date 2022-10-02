from django.contrib import admin

from .models import Ingredients, IngredientsAmount


@admin.register(Ingredients)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "measurement_unit",
    )
    ordering = ('name',)
    list_filter = ("name",)


@admin.register(IngredientsAmount)
class IngredientAmountAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "ingredient",
        "amount",
    )
