from django.shortcuts import render
from lib2to3.fixes.fix_input import context
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import *

# Create your views here.

# def menu(request):
#     return render(request,"menu.html")

def major(request):
    return render(request,"major.html")

def shop(request):
    GAmes = Game.objects.all()
    g=[]
    for i in GAmes:
        g.append(i.title + " | " + i.description + " Стоимость: " + str(i.cost))
    context = {'games': g}
    return render(request,"shop.html", context)

def basket(request):
    return render(request,"basket.html")


r1=""

def sign_up_by_django(request):
    global r1
    users = Buyer.objects.all()
    info={}
    info["error"] = ""
    context = info
    if request.method == "POST":
        info["error1"]="ошибка:"
        #получаем данные
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        print(users)
        print(f"username: {username}")
        print(f"password: {password}")
        print(f"repeat_password: {repeat_password}")
        print(f"age: {age}")
        if (password == repeat_password) and (int(age)>=18):
            r=0
            for i in users:
                if username == i.name:
                    r=1
                    break
            if r == 0:
                if r1 == "":
                    r1 = username
                    #Buyer.objects.create(name=username, balance=2000.05, age=age)
                    return HttpResponse(f"Приветствуем, {username}!")

        if password != repeat_password:
            info["error"] = "Пароли не совпадают"
            context = info
            return render(request, "registration_page.html", context)
        if int(age)<18:
            info["error"] = "Вы должны быть старше 18"
            context = info
            return render(request, "registration_page.html", context)
        if r==1:
            info["error"] = f"Пользователь {username} уже существует"
            context = info
            return render(request, "registration_page.html", context)
        #обновление страницы и добавление пользователя
        Buyer.objects.create(name=r1, balance=2000.05, age=age)
        r1=""
        info["error"] = f"Вы уже вводили эти данные"
        info["error1"] = ""
        context = info

    return render(request,"registration_page.html", context)


















from  .UserRegister import ContractForm
#users = ["user1", "user2", "user3"]
def sign_up_by_html(request):
    info = {}
    info["error"] = ""
    context = info
    if request.method == "POST":
        form = ContractForm(request.POST)
        info["form"] = form
        if form.is_valid():
            #обработка данных формы
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and int(age)>=18:
                if username not in users:
                    users.append(username)
                    info["form"] = ""
                    return HttpResponse(f"Приветствуем, {username}!")
            if password != repeat_password:
                info["error"] = "Пароли не совпадают"
                context = info
                return render(request, "registration_page.html", context)
            if int(age)<18:
                info["error"] = "Вы должны быть старше 18"
                info["form"] = ""
                context = info
                return render(request, "registration_page.html", context)
            if username in users:
                info["error"] = f"Пользователь {username} уже существует"
                info["form"] = ""
                context = info
                return render(request, "registration_page.html", context)
            #Http ответ пользователя
    else:
        form = ContractForm()
    info["form"] = ""
    return render(request, "registration_page.html", context)
