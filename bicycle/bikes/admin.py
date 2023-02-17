from django.contrib import admin
from .models import New_Bike
# импортируем QuerySet чтобы появлялмсь подсказки в функции change_sex_age
from django.db.models import QuerySet

# Register your models here.
# Tips:
# чтобы сменить язык в админке сайта, нужно выставить язык 'ru-RU'
# в settings.py, а также изменить язык отображения моделей при помощи
# verbose_name и verbose_name_plural в Meta классе модели.
#
# чтобы поменять "Администрирование Django" на что-то более приятное,
# прописываем admin.site.site_header = "Что-то приятное" в главном URL.
# Тоже изменить "Ад-е сайта", прописываем admin.site.index_title = "приятное".


# для отображенияя в админке регистрируем так, или как показано ниже/
@admin.register(New_Bike)
class New_BikeAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ['id',
                    'brand',
                    'model',
                    'veloformat',
                    'wheel_count',
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
                     'wheel_count',
                     'price',
                     'reliability']
    # начальная сорт-ка задается при помощи ordering, можно по неск. полям
    ordering = ['veloformat', ]
    # пагинация в админке
    list_per_page = 15
    # регистрируем ф-цию для быстрого изменения кол-ва колес, сама ф-ция ниже.
    # т.е. мы выбираем галочкой несколько полей, жмем изменить и ставится
    # дефолтное значение, в данном случае - 'обычный'
    actions = ['change_count_wheel']
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

# функция для быстрого изменения значения в админке, т.е. выделяем несколько
# записей и разом приcваиваем им какое-то значение. Сделаю быстрое изменение
# количества колес. Создаем функцию и регистрируем ее здесь же - выше.

    @admin.action(description='Изменить кол-во колес')
    def change_count_wheel(self, request, qs: QuerySet):
        # метод update позволяет обновить значения. Первым ставим значение,
        # которое хотим обновить
        qs.update(wheel_count=New_Bike.BI)
