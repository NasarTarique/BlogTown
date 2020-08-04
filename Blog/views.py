from django.shortcuts import render

from .models import Blog
# Create your views here.


def index(request):
    return render(request, "Blog/index.html")


def categories(request):
    return render(request, "Blog/categories.html")


def read(request, num):
    AllBlogs = Blog.objects.all()
    posts = []
    for x in range(0,4):
        posts.append(AllBlogs[x])

    return render(request, "Blog/reader.html", {
        "blog": Blog.objects.get(pk=num),
        "posts": posts
    })
