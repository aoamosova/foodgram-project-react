from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import F, Q

User = get_user_model()

class Subscriptions(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Подписчик',
        related_name='sudscriber',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор на которого подписан',
        related_name='sudscribed_authors',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural='Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=(
                    'user',
                    'author', 
                ),
                name='unique_subscribe',
            ),
            models.CheckConstraint(
                check=~Q(user=F('author')),
                name='self_subscription',
            ),
        ]
        ordering = ('-id',)

    def __str__(self):
        return f'{self.user}, подписан на {self.author}'