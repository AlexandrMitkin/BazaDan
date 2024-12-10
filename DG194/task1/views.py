from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post
from .models import News

# Create your views here.
a=3
def index(request):
    global a
    if request.method == "POST":
        a = request.POST.get('stroki')
    # получаем все посты
    posts = Post.objects.all().order_by("-created_at")
    # создаем пагинатор
    paginator = Paginator(posts, a)
    # получаем номер страницы, на которую переходит пользователь
    page_number = request.GET.get('page')
    # получаем посты для текущей страницы
    page_obj = paginator.get_page(page_number)
    # передаем контекст в шаблон

    return render(request, 'index.html', {'page_obj': page_obj})


def news(request):
    # получаем все посты
    newss = News.objects.all()
    # создаем пагинатор
    paginator = Paginator(newss, 3)
    # получаем номер страницы, на которую переходит пользователь
    page_number = request.GET.get('page')
    # получаем посты для текущей страницы
    page_obj = paginator.get_page(page_number)
    # передаем контекст в шаблон

    return render(request, 'news.html', {'page_obj': page_obj})

