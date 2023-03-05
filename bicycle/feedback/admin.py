from django.contrib import admin
from .models import FeedBack

# Регистрируем модель для отображения в админке
admin.site.register(FeedBack)
