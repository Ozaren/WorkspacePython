from django.shortcuts import render
from django.http import HttpResponse

import random as rand

# Create your views here.

def home(request):
    num = rand.randint(0, 1000000)
    return render(request, "base.html" , {"bool": False , "num": num})
