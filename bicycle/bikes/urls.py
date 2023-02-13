from django.urls import path

from . import views

app_name = 'bikes'

urlpatterns = [
    path('', views.index, name='index'),
    #path('bike/<int:bike_id>', views.bike_detail, name='bike_detail'),
]
