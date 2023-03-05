from django.urls import path

from feedback import views

app_name = 'feedback'

urlpatterns = [
    path('', views.feedback_posts, name='feedback_posts'),
    path('create/', views.create, name='create'),
]
