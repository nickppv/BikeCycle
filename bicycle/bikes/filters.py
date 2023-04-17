from .models import New_Bike

import django_filters


class BikeFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(
        lookup_expr='exact',
        label=' Выбрать брэнд'
        )
    veloformat = django_filters.CharFilter(
        lookup_expr='exact',
        label=' Формат велосипеда'
        )
    sex_age = django_filters.CharFilter(
        lookup_expr='exact',
        label=' Пол/Возраст'
        )
    price__gt = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gt',
        label=' Цена от'
        )
    price__lt = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lt',
        label=' Цена до'
        )

    class Meta:
        model = New_Bike
        fields = ['brand', 'sex_age', 'veloformat', 'sex_age', 'price']
