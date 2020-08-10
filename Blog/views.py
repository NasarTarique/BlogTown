from django.shortcuts import render

from .models import Blog
# Create your views here.


def index(request):
    return render(request, "Blog/index.html")


def categories(request):
    return render(request, "Blog/categories.html")

def about(request):
    return render(request, "Blog/about.html")    


def read(request, num):
    return render(request, "Blog/reader.html", {
        "blog": Blog.objects.get(pk=num)
    })
