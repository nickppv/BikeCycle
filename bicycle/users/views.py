# Импортируем CreateView, чтобы создать ему наследника
from django.views.generic import CreateView
# Функция reverse_lazy позволяет получить URL по параметрам функции path()
from django.urls import reverse_lazy
# Импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm


class SignUp(CreateView):
    # form_class — из какого класса берем форму
    form_class = CreationForm
    # после успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('bikes:index')
    # имя шаблона, куда будет передана переменная form с объектом HTML-формы
    template_name = 'users/signup.html'
