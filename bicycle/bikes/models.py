from django.db import models
from django.utils.text import slugify

# добавляем валидаторы, чтобы сделать ограничение на отрицат. значения в полях
from django.core.validators import MaxValueValidator, MinValueValidator


class New_Bike(models.Model):
    M = 'Мужской взрослый'
    MC = 'Мужской детский'
    W = 'Женский взрослый'
    WC = 'Женский детский'
    # второе значение идет админку в графу для выбора
    SEX_AGE = [
        (M, 'M'),
        (MC, 'MC'),
        (W, 'W'),
        (WC, 'WC'),
    ]
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
    brand = models.CharField(
        max_length=40,
        verbose_name='Производитель',
        )
    model = models.CharField(
        max_length=50,
        verbose_name='Модель',
        )
    sex_age = models.CharField(
        max_length=16,
        choices=SEX_AGE,
        default='Взрослый/мужской',
        verbose_name='Пол и возраст'
        )
    veloformat = models.CharField(
        max_length=15,
        default='mountain',
        verbose_name='Назначение'
        )
    wheel_count = models.CharField(
        max_length=3,
        default='BI',
        # создали поле выбора из огранич. списка. Остальные настройки выше.
        choices=WHEEL_COUNT,
        verbose_name='Кол-во колес'
        )
    sportsman = models.ForeignKey(
        'Sportsman',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    extensions = models.ManyToManyField(
        'Extension',
        blank=True,
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    picture = models.TextField(
        verbose_name='Изображение товара'
        )
    price = models.FloatField(
        validators=[MinValueValidator(0)],
        verbose_name='Стоимость'
        )
    reliability = models.IntegerField(
        # валидатор ограничивает создание значения меньше нуля и больше 100
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0,
        blank=True,
        verbose_name='Поломок на 100 шт.'
        )
    add_date = models.DateTimeField(
        # auto_now_add - добавляетдату и больше не меняет
        # auto_now будет обновлять дату каждый раз при редактировании
        auto_now_add=True,
        verbose_name='Дата добавления в БД'
        )
    brand_slug = models.SlugField(
        null=False,
        verbose_name='Slug Брэнда',
        blank=True,
    )
    model_slug = models.SlugField(
        null=False,
        unique=True,
        db_index=True,
        verbose_name='Slug Модели',
        blank=True,
    )

    def save(self, *args, **kwargs):
        self.brand_slug = slugify(self.brand)
        self.model_slug = slugify(self.model)
        super(New_Bike, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Велосипед'
        verbose_name_plural = 'Велосипеды'

    def __str__(self) -> str:
        return f'{self.brand} - {self.model}'


class Sportsman(models.Model):

    # создаем поле выбора для пола спортсмена
    M = 'MAN'
    W = 'WOMAN'
    CHOICE_SEX = [(M, 'Мужчина'), (W, 'Женщина')]

    name = models.CharField(
        max_length=50,
        verbose_name='Имя'
        )
    surname = models.CharField(
        max_length=50,
        verbose_name='Фамилия'
        )
    sex = models.CharField(
        max_length=7,
        choices=CHOICE_SEX,
        verbose_name='Пол'
    )
    birthday = models.DateField(
        verbose_name='Дата рождения'
    )
    all_distance = models.IntegerField(
        verbose_name='Пройденная за карьеру дистанция'
    )
    brand_distance = models.IntegerField(
        verbose_name='Пройденная дистанция за брэнд'
    )
    count_trophy = models.IntegerField(
        verbose_name='Количество наград',
        blank=True,
        null=True,
        default=0,
    )

    class Meta:
        verbose_name = 'Спортсмен'
        verbose_name_plural = 'Спортсмены'

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'


class Extension(models.Model):
    extension = models.CharField(
        verbose_name='Расширение для велосипеда',
        max_length=80,
    )
    brand_extension = models.CharField(
        verbose_name='Производитель',
        max_length=40,
    )
    description = models.TextField(
        verbose_name='Описание расширения',
        blank=True
    )

    class Meta:
        verbose_name = 'расширение'
        verbose_name_plural = 'Расширения'

    def __str__(self) -> str:
        return f'{self.extension}'
