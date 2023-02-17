from django.db import models


class New_Bike(models.Model):
    # чтобы создать поле выбора, можно просто создать список кортежей и
    # передать его в поле модели, но лучше создать отдельно константы
    # которые передать в кортежи, которые передадутся в поле модели.
    UNI = 'UNI'
    BI = 'BI'
    TRI = 'TRI'
    OTH = 'OTH'

    WHEEL_COUNT = [
        (UNI, 'Уницикл'),
        (BI, 'Обычный'),
        (TRI, 'Трицикл'),
        (OTH, 'Другое')
    ]
    brand = models.CharField(max_length=40,
                             verbose_name='Производитель')
    model = models.CharField(max_length=40,
                             verbose_name='Модель')
    sex_age = models.CharField(max_length=10,
                               default='Взрослый',
                               verbose_name='Пол и возраст')
    veloformat = models.CharField(max_length=15,
                                  default='Горный',
                                  verbose_name='Назначение')
    wheel_count = models.CharField(max_length=3,
                                   default='BI',
                                   choices=WHEEL_COUNT,
                                   verbose_name='Кол-во колес'
                                   )
    description = models.TextField(verbose_name='Описание')
    picture = models.TextField(verbose_name='Изображение товара')
    price = models.FloatField(verbose_name='Стоимость')
    reliability = models.IntegerField(default=0,
                                      blank=True,
                                      verbose_name='Поломок на 100 шт.')
    add_date = models.DateTimeField(auto_now=True,
                                    verbose_name='Дата добавления в БД')

    class Meta:
        verbose_name = 'Велосипед'
        verbose_name_plural = 'Велосипеды'

    def __str__(self) -> str:
        return f'{self.brand} - {self.model}'


class Sportsmens(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthday = models.DateField()
    distance = models.IntegerField()
    count_trophy = models.IntegerField
