from django.urls import path

from bikes import views

app_name = 'bikes'

urlpatterns = [
    path('', views.index, name='index'),
    path('veloformat/<format>/', views.veloformat, name='format'),
    path('about/', views.about, name='about'),
    path('brand/<slug:brand_slug>/', views.brand_group, name='brand_group'),
    path('brand/<slug:brand_slug>/<slug:model_slug>/',
         views.model_detail, name='model_detail'),
    path('for/<sex_age>/', views.sex_age_group, name='sex_age_group')
]
