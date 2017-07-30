from django.shortcuts import render
from django.http import HttpResponse

import random as rand

# Create your views here.

def home(request):
    num = rand.randint(0, 1000000)
    context = {"bool": False , "num": num}
    return render(request, "home1.html" , context)

def home2(request):
    num = rand.randint(0, 1000000)
    context = {}
    return render(request, "home2.html" , context)

def home3(request):
    num = rand.randint(0, 1000000)
    context = {}
    return render(request, "home3.html" , context)
