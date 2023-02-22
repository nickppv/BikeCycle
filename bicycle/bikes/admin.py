from django.contrib import admin
from .models import New_Bike, Sportsman, Extension
# импортируем QuerySet чтобы появлялмсь подсказки в функции change_sex_age
from django.db.models import QuerySet

# Register your models here.

# регистрируем модель. Можно так или есть другой вариант, как для модели ниже.
admin.site.register(Sportsman)
admin.site.register(Extension)


# Tips:
# чтобы сменить язык в админке сайта, нужно выставить язык 'ru-RU'
# в settings.py, а также изменить язык отображения моделей при помощи
# verbose_name и verbose_name_plural в Meta классе модели.
#
# чтобы поменять "Администрирование Django" на что-то более приятное,
# прописываем admin.site.site_header = "Что-то приятное" в главном URL.
# Тоже изменить "Ад-е сайта", прописываем admin.site.index_title = "приятное".


# создаем в админке фильтр по стоимости товара. Нам нужно опред-ть два метода:
# в первом методе lookups  мы установим знач-я, которые будем видеть в фильтре

class PriceFilter(admin.SimpleListFilter):
    title = 'Фильтр по стоимости'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return [
            ('0-4999', 'Одноразовый сегмент'),
            ('5000-9999', 'Полутораразовый+ сегмент'),
            ('10 000-24 999', 'Туда-сюда сегмент'),
            ('25 000-49 999', 'Дорого-богато сегмент'),
            ('50 000 - ', '%&@*ц-&@#й-#&%!ь сегмент'),
        ]

    def queryset(self, request, queryset):
        if self.value() == '0-4999':
            return queryset.filter(price__lt=5000)
        if self.value() == '5000-9999':
            return queryset.filter(price__gte=5000).filter(price__lt=5000)
        if self.value() == '10 000-24 999':
            return queryset.filter(price__gte=10000).filter(price__lt=25000)
        if self.value() == '25 000-49 999':
            return queryset.filter(price__gte=25000).filter(price__lt=50000)
        if self.value() == '50 000 - ':
            return queryset.filter(price__gte=50000)
        return queryset


# для отображенияя в админке регистрируем так, или как показано ниже
@admin.register(New_Bike)
class New_BikeAdmin(admin.ModelAdmin):
    # аттрибут fields влияет на отображение полей в разделе добавления или
    # редактирования записей. Если мы хотим видеть только определенные поля,
    # то заполняем ими fields
    # fields = ['',]

    # exclude = ['',] - противоположный аттрибут для fields. Он исключает
    # выбранные поля со страницы добавления или редактирования записей

    # вычисляемое поле, котрое мы записываем в словарь
    # prepopulated_fields = {slug: (model,)}

    readonly_fields = ['price']
    # аттрибут, который запрещает редактирование внесенных в него полей

    # Перечисляем поля, которые должны отображаться в админке
    list_display = ['id',
                    'brand',
                    'model',
                    'sex_age',
                    'veloformat',
                    'price']
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('brand', 'model',)
    # Добавляем возможность фильтрации по цене и надежности
    list_filter = [PriceFilter, 'reliability']
    # Это свойство сработает для всех колонок: где пусто — будет эта строка
    empty_value_display = '-пусто-'
    # возможность редактировать поля не заходя в детальную информацию.
    # Можно добавлять все поля, кроме первого и даты: первое является ссылкой
    # на наш объект (с.Егоров Артем), а второе дата добавления в БД
    list_editable = ['veloformat',
                     'sex_age',
                     'price',]
    # начальная сорт-ка задается при помощи ordering, можно по неск. полям
    ordering = ['brand', ]
    # пагинация в админке
    list_per_page = 15
    # создаем фильтр для связанного поля extensions-bicycle. После добавления
    # filter_horizontal, в записи о велосипеде появится дополнительное окно со
    # всеми возможными расширениями для велосипедов, которые удобно добавлять.
    filter_horizontal = ['extensions']
    # регистрируем ф-цию для быстрого изменения кол-ва колес, а также
    # (сброс количества поломок), сама ф-ция ниже.
    # т.е. мы выбираем галочкой несколько полей, жмем изменить и ставится
    # дефолтное значение, в данном случае - 'обычный'
    actions = ['change_count_wheel', 'skip_reliability']
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

    @admin.action(description='Изменить количество колес')
    def change_count_wheel(self, request, qs: QuerySet):
        # метод update позволяет обновить значения. Первым ставим значение,
        # которое хотим обновить
        qs.update(wheel_count=New_Bike.BI)

    @admin.action(description='Сбросить количество поломок на ноль')
    def skip_reliability(self, request, qs: QuerySet):
        # метод update позволяет обновить значения. Первым ставим значение,
        # которое хотим обновить
        qs.update(reliability=0)
