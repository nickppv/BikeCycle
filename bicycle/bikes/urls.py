from django.urls import path

from bikes import views

app_name = 'bikes'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('<slug:brand_slug>/', views.brand_group, name='brand_group'),
    path('<slug:brand_slug>/<slug:model_slug>/',
         views.model_detail, name='model_detail'),
]
