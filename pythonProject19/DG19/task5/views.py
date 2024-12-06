from django.shortcuts import render
from django.http import HttpResponse
#from django.views.generic import TemplateView
#from .forms import ContractForm
from  .UserRegister import ContractForm



users=["user1", "user2", "user3"]
r=["user1", "user2", "user3"]

def sign_up_by_django(request):
    #users = ["user1", "user2", "user3"]
    info={}
    info["error"] = ""
    context = info
    if request.method == "POST":
        #получаем данные
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        print(f"username: {username}")
        print(f"password: {password}")
        print(f"repeat_password: {repeat_password}")
        print(f"age: {age}")
        if (password == repeat_password) and (int(age)>=18):
            if username not in users:
                if username not in r:
                    r.append(username)
                    return HttpResponse(f"Приветствуем, {username}!")

        if password != repeat_password:
            info["error"] = "Пароли не совпадают"
            context = info
            return render(request, "registration_page.html", context)
        if int(age)<18:
            info["error"] = "Вы должны быть старше 18"
            context = info
            return render(request, "registration_page.html", context)
        if username in users:
            info["error"] = f"Пользователь {username} уже существует"
            context = info
            return render(request, "registration_page.html", context)
        #Http ответ пользователя
        l=len(r)
        users.append(r[l-1])
        info["error"] = f"Вы не ввели данные"
        context = info
        return render(request, "registration_page.html", context)

    return render(request,"registration_page.html", context)

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




















def registration_page(request):
    error ="10"
    context = {'error': error}
    if request.method == "POST":
        #получаем данные
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        print(f"username: {username}")
        print(f"password: {password}")
        print(f"repeat_password: {repeat_password}")
        print(f"age: {age}")

    #если это GET
    return render(request, "registration_page.html",context)











# def registration_page(request):
#     name = request.GET.get('name', 'Guest')
#     return HttpResponse(f"Hello, {name}!")

# def registration_page(request):
#     if request.method == "POST":
#         message = request.POST.get("message", "")
#         return HttpResponse(f"Your said: {message}")
#     return render(request, "registration_page.html")

# def registration_page(request):
#     return HttpResponse("Hello!", status = 400, reason="!!!")

# def registration_page(request):
#     if request.method == "POST":
#         #получаем данные
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         subscribe = request.POST.get('subscribe')=="on"
#
#         print(f"Name: {name}")
#         print(f"Email: {email}")
#         print(f"Message: {message}")
#         print(f"Subscribe: {subscribe}")
#
#         #Http ответ пользователя
#         return HttpResponse("Форма успешно отправлена!")
#
#     #если это GET
#     return render(request, "registration_page.html")

# def registration_page(request):
#     if request.method == "POST":
#         form = ContractForm(request.POST)
#         if form.is_valid():
#             #обработка данных формы
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             subscribe = form.cleaned_data['subscribe']
#     else:
#         form = ContractForm()
#     #если это GET
#     return render(request, "registration_page.html",{"form":form})

