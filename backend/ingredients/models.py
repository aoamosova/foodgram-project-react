from django.db import models


class Ingredients(models.Model):
    """ Ингридиенты """
    name = models.CharField(
        max_length=200,
        verbose_name='Название',
        null=False,
    )
    measurement_unit = models.CharField(
        max_length=20,
        verbose_name='Единица измерения',
        null=False,
    )

    class Meta:
        verbose_name='Ингредиент'
        verbose_name_plural='Ингредиенты'

    def __str__(self):
        return {self.name}, {self.measurement_unit}

    
class IngredientsVolume(models.Model):
    """Колличество ингридиентов"""
    ingredient = models.ForeignKey(
        Ingredients,
        verbose_name='Ингредиент',
        on_delete=models.CASCADE,
    )
    volume = models.PositiveIntegerField(
        verbose_name='Количество'
    )
    
    class Meta:
        verbose_name='Количество ингридиента'
        verbose_name_plural='Количество ингридиентов'

    def __str__(self):
        return {self.ingredient} - {self.volume}
