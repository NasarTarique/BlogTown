from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "Blog/index.html")


def categories(request):
    return render(request, "Blog/categories.html")


def read(request, num):
    return render(request, "Blog/reader.html")
