# from multiprocessing.managers import public_methods
#
# from Tools.scripts.patchcheck import status
from django.shortcuts import render, get_object_or_404

from .models import Post


# Create your views here.
# def post_list(request):
#     posts = Post.published.all()
#     return render(request, "blog/post/list.html", {"posts": posts})
#
# def post_detail(request, year, month, day, post):
#     post = get_object_or_404(Post, slug = post, status = "published", public_year = year,
#                              publish_month = month, publish_day = day)
#     return render(request, "blog/post/detail.html", {"post":post})

