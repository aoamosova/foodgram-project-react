from django.core import validators
from django.db import models


class Ingredients(models.Model):
    """ Ингридиенты """
    name = models.CharField(
        max_length=200,
        verbose_name='Название',
    )
    measurement_unit = models.CharField(
        max_length=20,
        verbose_name='Единица измерения',
    )

    class Meta:
        verbose_name='Ингредиент'
        verbose_name_plural='Ингредиенты'

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'

    
class IngredientsAmount(models.Model):
    """Колличество ингридиентов"""
    ingredient = models.ForeignKey(Ingredients, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField(
        validators=[validators.MinValueValidator(1, 'Не может быть менее 1')]
    )
    
    class Meta:
        verbose_name='Количество ингридиента'
        verbose_name_plural='Количество ингридиентов'

    def __str__(self):
        return f'{self.ingredient} * {self.amount}'
