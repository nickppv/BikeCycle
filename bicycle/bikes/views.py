from django.core.paginator import Paginator
from django.shortcuts import  get_object_or_404, redirect, render
from .models import New_Bikes

# постоянная с количеством постов на странице
AMOUNT_POSTS = 15


def index(request):
    all_details = New_Bikes.objects.all()
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
