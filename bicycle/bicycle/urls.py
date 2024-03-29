"""bicycle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static

from bicycle import settings

# настройки для отображения в админке вместо слов "Администрирование" и др.
admin.site.site_header = 'ГлаВВелосипеД'
admin.site.index_title = 'Вы - прекрасный администратор'

urlpatterns = [
    # расширяем и изменяем работу встроенного приложения django.contrib.auth,
    # если какой-то URL не обнаружится в приложении users — Django пойдёт
    # искать его в django.contrib.auth - этот путь идет ниже, через один.
    path('auth/', include('users.urls', namespace='users')),
    # подключаем 'auth' чтобы дать пользователям доступ к страницам приложения
    # вместо префикса auth/ можно установить любой другой, но хорошим тоном
    # будет установить префикс, который совпадает с именем приложения,
    # обрабатывающего URL
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('bikes.urls', namespace='bikes')),
    path('feedback/', include('feedback.urls', namespace='feedback')),
    path('captcha/', include('captcha.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# переопределяем страницы ошибок, вместо стандартных делаем свои - красивые!
handler404 = "bikes.views.page_not_found" # noqa
handler500 = "bikes.views.server_error"   # noqa
