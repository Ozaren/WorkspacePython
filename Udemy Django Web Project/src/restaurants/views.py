from django.shortcuts import render
from django.http import HttpResponse

from django.views import View
from django.views.generic import TemplateView, ListView

from .models import Restaraunt

# Create your views here.

def rest_list(request):
    queryset = Restaraunt.objects.all()
    
    context = {
        "object_list" : queryset
    }
    return render(request , "restaurants/restaurants_list.html" , context)

class RestarauntListView(ListView):
    template_name = "restaurants/restaurants_list.html"
    queryset = Restaraunt.objects.all()
    
    