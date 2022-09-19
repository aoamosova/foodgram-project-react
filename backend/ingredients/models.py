from tabnanny import verbose
from django.db import models


class Ingredients(models.Model):
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
        return self.name