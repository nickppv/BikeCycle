from django.contrib import admin
from .models import New_Bike

# Register your models here.


# для отображенияя в админке регистрируем так, или как показано ниже/
@admin.register(New_Bike)
class New_BikeAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ['id',
                    'brand',
                    'model',
                    'veloformat',
                    'price',
                    'reliability',
                    'rating',
                    'add_date']
    # Добавляем интерфейс для поиска по тексту постов
    # search_fields = ('brand', 'model',)
    # Добавляем возможность фильтрации по дате
    # list_filter = ('pub_date',)
    # Это свойство сработает для всех колонок: где пусто — будет эта строка
    empty_value_display = '-пусто-'
    # возможность редактировать поля не заходя в детальную информацию.
    # Можно добавлять все поля, кроме первого и даты: первое является ссылкой
    # на наш объект (с.Егоров Артем), а второе дата добавления в БД
    list_editable = ['brand',
                     'model',
                     'veloformat',
                     'price',
                     'reliability']
    # начальная сорт-ка задается при помощи ordering, можно по неск. полям
    ordering = ['veloformat', ]
    # пагинация в админке
    list_per_page = 15
    # создаем вычисляемое поле. Вторым арг-м добавляем экз-р класса New_Bikes
    # - и эту переменную мы можем называть как угодно.
    # Если не добавлять метод description, то названием колонки останется
    # 'rating' - по имени функции. Аннотируем переменную bike, чтобы прог-ма
    # подсказывала варианты продолжения кода.

    # декоратор для возможности сортировки по полю аннотации.
    # выбираем reliability, т.к. у них прямая зависимость.
    # description для красивого описания поля.
    @admin.display(ordering='reliability', description='Качество')
    def rating(self, breaking: New_Bike):
        if breaking.reliability <= 2:
            return 'Это очень надежный товар'
        if breaking.reliability <= 5:
            return 'Достаточно надежный товар'
        if breaking.reliability <= 8:
            return 'Среднее качество'
        if breaking.reliability <= 10:
            return 'Среднее качество товар'
        return 'Плохое качество'

# можно зарегистрировать так, или декоратором
# admin.site.register(New_Bike, New_BikeAdmin)


# Tips:
# чтобы сменить язык в админке сайта, нужно выставить язык 'ru-RU'
# в settings.py, а также изменить язык отображения моделей при помощи
# verbose_name и verbose_name_plural в Meta классе модели.
#
# чтобы поменять "Администрирование Django" на что-то более приятное,
# прописываем admin.site.site_header = "Что-то приятное" в главном URL.
# Тоже изменить "Ад-е сайта", прописываем admin.site.index_title = "приятное".
