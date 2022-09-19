from django.db import models
from django.core import validators
from django.contrib.auth import get_user_model

from tags.models import Tags
from ingredients.models import Ingredients

User = get_user_model()

class Recipes(models.Model):
    tags = models.ManyToManyField(
        Tags,
        verbose_name='Тэги'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='recipes',
    )
    ingredients = models.ManyToManyField(
        Ingredients,
        verbose_name='Ингридиенты',
        related_name='recipes',
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
    )
    image = models.ImageField(
        upload_to='recipes/',
        verbose_name='Картинка',
    )
    text = models.TextField(
        verbose_name='Описание',
    )
    cooking_time = models.PositiveSmallIntegerField(
        default=1,
        validators=[validators.MinLengthValidator(1, 'Укажите время приготовления в минутах')],
        verbose_name='Время приголовления в минутах',
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural='Рецепты'

    def __str__(self):
        return self.name