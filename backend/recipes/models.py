from tabnanny import verbose
from django.db import models
from django.core import validators

from tags.models import Tags
from users.models import User
from ingredients.models import Ingredients


class Recipes(models.Model):
    tags = models.ManyToManyField(
        Tags,
        verbose_name='Тэги',
        related_name='recipes',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='recipes',
    )
    ingredients = models.ManyToManyField(
        Ingredients,
        verbose_name='Список ингридиентов',
        related_name='recipes',
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
    )
    image = models.ImageField(
        upload_to='recipes/images/',
        verbose_name='Картинка',
    )
    text = models.TextField(
        verbose_name='Описание',
    )
    cooking_time = models.PositiveSmallIntegerField(
        default=1,
        validators=[validators.MinValueValidator(1, 'Укажите время приготовления в минутах')],
        verbose_name='Время приголовления в минутах',
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Рецепт'
        verbose_name_plural='Рецепты'

    def __str__(self):
        return f'{self.name}'


class Favourites(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipes,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='favourites'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Избранный рецепт'
        verbose_name_plural = 'Избранные рецепты'
        
    def __str__(self):
        return f'{self.user} добавил в избранное {self.recipe}'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipes,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='shoppingcart'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Список покупок'
        
    def __str__(self):
        return f'{self.user} добавил в список покупок {self.recipe}'
