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
    path('password_reset/', PasswordResetView.as_view
         (template_name='users/password_reset_form.html'),
         name='password_reset_form'),
]
