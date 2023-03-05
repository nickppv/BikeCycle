from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import FeedBack
from .forms import FeedbackForm


AMOUNT_POSTS = 10


def feedback_posts(request):
    all_obj = FeedBack.objects.all()
    # создаем экземпляр класса Paginator и указываем количество товаров.
    paginator = Paginator(all_obj, AMOUNT_POSTS)
    # получаем номер текущей страницы
    page_number = request.GET.get('page')
    # формируем список элементов текущей страницы
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'title': 'Страница отзывов',
        'all_obj': all_obj,
    }
    return render(request, 'feedback/feedback.html', context)


@login_required
def create(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        feedback = form.save(commit=False)
        feedback.author = request.user
        feedback.save()
        return redirect('feedback:feedback_posts')
    context = {'form': form}
    return render(request, 'feedback/create.html', context)
