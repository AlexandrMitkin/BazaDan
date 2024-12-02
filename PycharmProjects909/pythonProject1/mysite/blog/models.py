from Tools.scripts.patchcheck import status
from django.db import models
from django.utils import timezone #часовые пояса
from django.contrib.auth.models import User # аунтификация пользоавтелей


# Create your models here.
# class PublishedManager(models.Model):
#     def get_queryset(self):
#         return super().get_queryset.filter(status = 'published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250) #заголовок статьи
    slug = models.SlugField(max_length=250, unique_for_date='publish') #URL статьи используя уникальную дату публикации
    author = models.ForeignKey(User, on_delete=models.CASCADE, #внешний ключ один ко многим
                                related_name='blog_posts')
    body = models.TextField() #содержание статьи
    publish = models.DateField(default=timezone.now) #дата публикации статьи
    created = models.DateTimeField(auto_now_add=True) #дата создания статьи
    updated = models.DateTimeField(auto_now=True) #дата и период, когда статья была отредактирована
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft') #статус статьи
    # objects = models.Manager() #менеджер по умочанию
    # published = PublishedManager() #наш новый менеджер



    class Meta: #Мета
        ordering = ('-publish',)
    def __str__(self):
        return self.title #вовращает значение понятное для человека


