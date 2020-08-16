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
    AllBlogs = Blog.objects.all()
    posts = []
    for x in range(0, 6):
        posts.append(AllBlogs[x])

    return render(request, "Blog/reader.html", {
        "blog": Blog.ebjects.get(pk=num),
        "posts": posts
    })

def contact(request):
    if request.method == 'POST':
        return render(request, "Blog/contact.html",{
            "method":'post'
        })
    else:
        return render(request, "Blog/contact.html", {
        "method":'get'
    })


