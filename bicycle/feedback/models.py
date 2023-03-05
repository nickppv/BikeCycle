from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class FeedBack(models.Model):
    text = models.TextField(
        verbose_name='Текст отзыва',
        max_length=1000,
        help_text='Напишите простой и понятный отзыв',
        )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
        )
    author = models.ForeignKey(
        User,
        max_length=50,
        on_delete=models.CASCADE,
        verbose_name='Имя пользователя'
        )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self) -> str:
        return f'{self.text[:75]} ...'
