from django.urls import path

from bikes import views

app_name = 'bikes'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('<slug:brand_group>/', views.brand_group, name='brand_group'),
    path('<slug:brand_group>/<slug:model_info>/',
         views.model_detail, name='model_info'),
]
