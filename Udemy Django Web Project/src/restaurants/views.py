from django.shortcuts import render
from django.http import HttpResponse

from django.views import View
from django.views.generic import TemplateView

import random as rand

# Create your views here.

class HomeView(TemplateView):
    template_name = "home1.html"
    
    def get_context_data(self, **kwargs):
        num = rand.randint(0, 1000000)
        context = {"bool": False , "num": num}
        return context