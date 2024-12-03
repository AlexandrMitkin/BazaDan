from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def major(request):
    name1 = "главная"
    name2 = "магазин"
    name3 = "корзина"
    context = {
        'major': name1,
        'shop': name2,
        'basket': name3,
    }
    return render(request,"major.html", context)

def shop(request):
    context = {

    }
    return render(request,"shop.html", context)

def basket(request):
    context={

    }
    return render(request,"basket.html", context)