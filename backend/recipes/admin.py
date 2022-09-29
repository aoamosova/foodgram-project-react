from django.contrib import admin

from .models import Favorite, Recipes, ShoppingCart


@admin.register(Recipes)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "author",
        "count_favorites",
    )
    list_filter = (
        "author",
        "name",
        "tags",
    )

    def count_favorites(self, obj):
        return obj.favorite.count()


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "user",
        "recipe",
    )


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "user",
        "recipe",
    )
