from django.shortcuts import  get_object_or_404, redirect, render
from .models import New_Bikes


def index(request):
    all_details = New_Bikes.objects.all()
    context = {
        'all_details': all_details,
        'title': 'ГлаВВелосипеД',
    }
    return render(request, 'bikes/index.html', context)
