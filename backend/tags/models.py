from django.db import models


class Tags(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название',
        unique=True,
        null=False,        
    )
    color = models.CharField(
        max_length=16,
        verbose_name='Цветовой HEX-код',
        unique=True,
        null=False,
    )
    slug = models.SlugField(
        verbose_name='Уникальный номер',
        max_length=50,
        unique=True,
        null=False
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural='Теги'

    def __str__(self):
        return self.name
