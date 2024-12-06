from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# def menu(request):
#     return render(request,"menu.html")

def major(request):
    return render(request,"major.html")

def shop(request):
    context = {'games': ["Atomic Heart   ", "Cyberpunk 2077", "PayDay 2"]}
    return render(request,"shop.html", context)

def basket(request):
    return render(request,"basket.html")

# def base(request):
#     return render(request, "basket.html")
