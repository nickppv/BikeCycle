from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

# User = get_user_model()


# class FeedBack(models.Model):
#     text = models.TextField(
#         verbose_name='Текст отзыва'
#         )
#     pub_date = models.DateTimeField(
#         auto_now_add=True,
#         verbose_name='Дата публикации'
#         )
#     author = models.ForeignKey(
#         User,
#         max_length=50,
#         on_delete=models.CASCADE,
#         verbose_name='Имя пользователя'
#         )
