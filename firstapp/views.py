from django.shortcuts import render
from django.db import models
from .models import cal


# Create your views here.

def index(request):
       return render(request ,'home.html')

def calculating(request):
    return render(request,'calculating.html')

def caled(request):

    value_a = request.POST['valueA']
    value_b = request.POST['valueB']
    consequence = int(value_a)+int(value_b)
    cal.objects.create(value_a=value_a,value_b=value_b,result=consequence)
    return render(request,'result.html',context={'data': consequence})
