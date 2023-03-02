from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .models import New_Bike, Sportsman

# постоянная для пагинатора с кол-вом постов на странице
AMOUNT_POSTS = 15


def index(request):
    all_details = New_Bike.objects.all()
    # создаем экземпляр класса Paginator и указываем количество товаров.
    paginator = Paginator(all_details, AMOUNT_POSTS)
    # получаем номер текущей страницы
    page_number = request.GET.get('page')
    # формируем список элементов текущей страницы
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'all_details': all_details,
        'title': 'ГлаВВелосипеД',
    }
    return render(request, 'bikes/index.html', context)


# страница со всеми байками выбранного брэнда
def brand_group(request, brand_slug):
    brand_group = New_Bike.objects.filter(brand_slug=brand_slug)
    paginator = Paginator(brand_group, AMOUNT_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'brand_group': brand_group,
        'page_obj': page_obj,
    }
    return render(request, 'bikes/brand_group.html', context)


def model_detail(request, brand_slug, model_slug):
    brand_group = New_Bike.objects.filter(brand_slug=brand_slug)
    model_detail = New_Bike.objects.filter(model_slug=model_slug)
    context = {
        'brand_group': brand_group,
        'model_detail': model_detail,
    }
    return render(request, 'bikes/model_detail.html', context)


def veloformat(request, format):
    group = New_Bike.objects.filter(veloformat=format)
    paginator = Paginator(group, AMOUNT_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'bikes/format.html', context)


# формируем список для определенной поло-возрастной группы
def sex_age_group(request, sex_age):
    group = New_Bike.objects.filter(sex_age=sex_age)
    paginator = Paginator(group, AMOUNT_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'bikes/sex_age_group.html', context)


# информация о сайте
def about(request):
    return render(request, 'about/about.html')


#  создаем функцию для отображения нашего варианта страницы ошибки 404
def page_not_found(request, exception):
    return render(request,
                  'about/404.html',
                  {'path': request.path},
                  status=404)


#  создаем функцию для отображения нашего варианта страницы ошибки 500
def server_error(request):
    return render(request, 'about/500.html', status=500)
