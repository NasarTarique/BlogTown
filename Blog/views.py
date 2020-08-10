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
    for x in range(0, 6):
        posts.append(AllBlogs[x])

    return render(request, "Blog/reader.html", {
        "blog": Blog.objects.get(pk=num),
        "posts": posts
    })

def contact(request):
    return render(request, "Blog/contact.html")

def about(request):
    return render(request, "Blog/about.html")
