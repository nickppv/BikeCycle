from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('logout/', LogoutView.as_view(template_name='users/logout.html'),
         name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='users/login.html'),
         name='login'),
    # смена пароля
    path('password_change/', PasswordChangeView.as_view
         (template_name='users/password_change_form.html'),
         name='password_change'),
    # смена пароля прошла успешно
    path('password_change/done/', PasswordChangeDoneView.as_view
         (template_name='users/password_change_done.html'),
         name='password_change_done'),
    # сброс пароля
    path('password_reset/', PasswordResetView.as_view
         (template_name='users/password_reset_form.html'),
         name='password_reset_form'),
    # уведомление об отправке ссылки для восстановления пароля на почту
    path('password_reset/done/', PasswordResetDoneView.as_view
         (template_name='users/password_reset_done.html'),
         name='reset_done'),
    # подтверждение сброса пароля
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view
         (template_name='users/password_reset_confirm.html'),
         name='reset_confirm'),
    # уведомление, что пароль изменен
    path('reset/done/', PasswordResetCompleteView.as_view
         (template_name='users/password_reset_complete.html'),
         name='reset_complete'),
]
