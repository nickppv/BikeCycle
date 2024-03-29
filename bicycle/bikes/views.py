from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from .models import New_Bike
from .filters import BikeFilter

import random
from datetime import datetime


# постоянная для пагинатора с кол-вом постов на странице
AMOUNT_POSTS = 18


def values_for_filter():
    distinct_brand = New_Bike.objects.values('brand').distinct()
    distinct_veloformat = New_Bike.objects.values('veloformat').distinct()
    distinct_sex_age = New_Bike.objects.values('sex_age').distinct()
    context = {
        'distinct_brand': distinct_brand,
        'distinct_veloformat': distinct_veloformat,
        'distinct_sex_age': distinct_sex_age,
    }
    return context


def index(request):
    all_details = New_Bike.objects.all().order_by('price')
    # создаем экземпляр класса Paginator и указываем количество товаров.
    paginator = Paginator(all_details, AMOUNT_POSTS)
    # получаем номер текущей страницы
    page_number = request.GET.get('page')
    # формируем список элементов текущей страницы
    page_obj = paginator.get_page(page_number)
    # выборка уникальных полей брэнда


    # устанавливаем зерно для модуля random, меняется каждый час
    bonus_bike_random_seed = datetime.now().strftime('%y%m%d%H')
    random.seed(bonus_bike_random_seed)
    discount = random.randrange(10, 51)
    random_id = random.choice(New_Bike.objects.values('id'))['id']
    # выбор велосипеда со скидкой на ближайший час
    choose_happy_bike = New_Bike.objects.filter(id=random_id)
    # цена велосипеда со скидкой
    new_price = round((choose_happy_bike.values('price')[0]['price'] * (
        1-discount/100)), 1)

    context = {
        'page_obj': page_obj,
        'all_details': all_details,
        'discount': discount,
        'new_price': new_price,
        'choose_happy_bike': choose_happy_bike,
        'title': 'ГлаВВелосипеД',
    } | values_for_filter()
    return render(request, 'bikes/index.html', context)


def filter(request):
    filter = BikeFilter(request.GET, queryset=New_Bike.objects.all())

    paginator = Paginator(filter.qs, AMOUNT_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'filter': filter,
        'page_obj': page_obj,
        } | values_for_filter()
    return render(request, 'bikes/page_filter.html', context)


# страница со всеми байками выбранного брэнда
def brand_group(request, brand_slug):
    brand_group = New_Bike.objects.filter(brand_slug=brand_slug)
    paginator = Paginator(brand_group, AMOUNT_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'brand_group': brand_group,
        'page_obj': page_obj,
    } | values_for_filter()
    return render(request, 'bikes/brand_group.html', context)


def model_detail(request, brand_slug, model_slug):
    brand_group = New_Bike.objects.filter(brand_slug=brand_slug)
    model_detail = New_Bike.objects.filter(model_slug=model_slug)
    title = get_object_or_404(New_Bike, model_slug=model_slug)
    context = {
        'title': title,
        'brand_group': brand_group,
        'model_detail': model_detail,
    } | values_for_filter()
    return render(request, 'bikes/model_detail.html', context)


def veloformat(request, format):
    group = New_Bike.objects.filter(veloformat=format)
    paginator = Paginator(group, AMOUNT_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    } | values_for_filter()
    return render(request, 'bikes/format.html', context)


# формируем список для определенной половозрастной группы
def sex_age_group(request, sex_age):
    group = New_Bike.objects.filter(sex_age=sex_age)
    paginator = Paginator(group, AMOUNT_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    } | values_for_filter()
    return render(request, 'bikes/sex_age_group.html', context)


# страница с велосипедами схожей ценовой категории - +/-3000
def price_group(request, price):
    if float(price) <= 3000:
        title = float(price)+2000
    else:
        title = price
    price_group = New_Bike.objects.filter(
        price__gte=float(price)-3000).filter(
        price__lte=float(price)+3000)
    paginator = Paginator(price_group, AMOUNT_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        # выношу в title стоимость +/- 3000 от выбранной стоимости,
        # если нажать на цену - на странице отобразятся все велосипеды +/- 3000
        'title': f'цена от {float(title)-3000} до {float(title)+3000}',
        'price_group': price_group,
        'page_obj': page_obj,
    } | values_for_filter()
    return render(request, 'bikes/price_group.html', context)


def bonus_bike(request):
    '''функция для отображения случайного велосипеда из БД со скидкой,
    меняется каждый час'''
    # создаем зерно на основе даты, которое будет меняться каждый час, день...
    bonus_bike_random_seed = datetime.now().strftime('%y%m%d%H')
    random.seed(bonus_bike_random_seed)
    discount = random.randrange(10, 51)
    random_id = random.choice(New_Bike.objects.values('id'))['id']
    choose_happy_bike = New_Bike.objects.filter(id=random_id)
    new_price = round((choose_happy_bike.values('price')[0]['price'] *
                      (1-discount/100)), 1)
    context = {
        'discount': discount,
        'new_price': new_price,
        'choose_happy_bike': choose_happy_bike,
    } | values_for_filter()
    return render(request, 'bikes/bonus_bike.html', context)


# информация о сайте
def about(request):
    context = {'title': 'Информация о сайте'}
    return render(request, 'about/about.html', context)


#  создаем функцию для отображения нашего варианта страницы ошибки 404
def page_not_found(request, exception):
    return render(request,
                  'about/404.html',
                  {'path': request.path},
                  status=404)


#  создаем функцию для отображения нашего варианта страницы ошибки 500
def server_error(request):
    return render(request, 'about/500.html', status=500)
