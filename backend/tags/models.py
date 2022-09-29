from django.db import models


class Tags(models.Model):
    """Тэги"""
    name = models.CharField(
        max_length=200,
        verbose_name='Название',        
    )
    color = models.CharField(
        max_length=16,
        verbose_name='Цветовой HEX-код',
    )
    slug = models.SlugField(
        verbose_name='Уникальный номер',
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural='Теги'
        constraints = [
            models.UniqueConstraint(
                fields=(
                    "name",
                    "color",
                ),
                name="unique_tag_name_color",
            )
        ]

    def __str__(self):
        return self.slug[:20]
