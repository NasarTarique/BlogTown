from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import Http404


import ssl
from smtplib import SMTP
from . import config 

from .models import Blog


def index(request):
    return render(request, "Blog/index.html")


def categories(request):
    return render(request, "Blog/categories.html")


def about(request):
    return render(request, "Blog/about.html")    


def read(request, num):
    AllBlogs = Blog.objects.filter(mode="Published")
    posts = []
    for x in range(0, 6):
        posts.append(AllBlogs[x])

    return render(request, "Blog/reader.html", {
        "blog": Blog.objects.filter(mode="Published").get(pk=num),
        "posts": posts
    })


def contact(request):

    def send_mail(name, email, content):
        context = ssl.create_default_context()
        with SMTP("smtp.gmail.com") as smtp:
            smtp.ehlo()
            smtp.starttls(context=context)
            smtp.ehlo()
            subject = 'BlogTown Contact'
            body = f"{name}\n\n{email}\n\n{content}" 
            msg = f"Subject:{subject}\n\n{body}"
            smtp.login(config.EMAIL_ADDRESS, config.EMAIL_PWD)
            smtp.sendmail(config.EMAIL_ADDRESS, config.TEST_MAIL, msg)
    
    if request.method == 'POST':
        send_mail(request.POST.get('name'), request.POST.get('mail'), request.POST.get('content'))
        return render(request, "Blog/contact.html",{
            "method": 'post'
        })
    else:
        return render(request, "Blog/contact.html", {
        "method":'get'
    })


def post(request):
    genre = request.GET.get("genre")
    if genre == "anime":
        allblogs = Blog.objects.filter(genre="Anime")
    elif genre == "movies":
        allblogs = Blog.objects.filter(genre="Movies")
    elif genre == "series":
        allblogs = Blog.objects.filter(genre="Series")
    elif genre == "novels":
        allblogs = Blog.objects.filter(genre="Novels")
    elif genre == "sports":
        allblogs = Blog.objects.filter(genre="Sports")
    elif genre == "poetry":
        allblogs = Blog.objects.filter(genre="Poetry")
    else:
        allblogs = Blog.objects.all()
    paginator = Paginator(allblogs, 2)
    page_number = int(request.GET.get('page'))
    page_obj = paginator.get_page(page_number)
    posts = []
    for x in range(0, len(page_obj), 2):
        if (x+1) >= len(page_obj):
            tup = tuple((page_obj[x], None))
            print(tup)
        else:
            tup = tuple((page_obj[x], page_obj[x+1]))
        posts.append(tup)
    if page_number > paginator.num_pages:
        return None
    else:
        return render(request, "Blog/posts.html",{
            'posts': posts
        })


def list(request):
    allblogs = Blog.objects.all()
    paginator = Paginator(allblogs, 4)
    page_number = int(request.GET.get('page', 1))
    page_obj = paginator.get_page(page_number)
    posts = []
    for x in range(0, len(page_obj), 2):
        if (x+1) >= len(page_obj):
            tup = tuple((page_obj[x], None))
        else:
            tup = tuple((page_obj[x], page_obj[x+1]))
        posts.append(tup)
    if page_number > paginator.num_pages:
        return None
    return render(request, "Blog/list.html", {
        'page_obj': posts,
        'genre': "BLOGS"
    })

def genre(request, genre):
    if genre == "anime":
        allblogs = Blog.objects.filter(genre="Anime")
    elif genre == "movies":
        allblogs = Blog.objects.filter(genre="Movies")
    elif genre == "series":
        allblogs = Blog.objects.filter(genre="Series")
    elif genre == "novels":
        allblogs = Blog.objects.filter(genre="Novels")
    elif genre == "sports":
        allblogs = Blog.objects.filter(genre="Sports")
    elif genre == "poetry":
        allblogs = Blog.objects.filter(genre="Poetry")
    paginator = Paginator(allblogs, 4)
    page_number = int(request.GET.get('page', 1))
    page_obj = paginator.get_page(page_number)
    posts = []
    for x in range(0, len(page_obj), 2):
        if (x+1) >= len(page_obj):
            tup = tuple((page_obj[x], None))
        else:
            tup = tuple((page_obj[x], page_obj[x+1]))
        posts.append(tup)
    if page_number > paginator.num_pages:
        return None
    return render(request, "Blog/list.html", {
        'page_obj': posts,
        'genre': genre 
    })
