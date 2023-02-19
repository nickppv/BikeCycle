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
def brand_group(request, brand_group):
    group_models = New_Bike.objects.filter(brand=brand_group)
    context = {
        'group': group_models,
    }
    return render(request, 'bikes/brand_group.html', context)


def model_detail(request, brand_slug):
    group_models = New_Bike.objects.filter(brand=brand_slug)

    context = {
        'group': group_models,
    }
    return render(request, 'bikes/model_detail.html', context)


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
