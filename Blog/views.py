from django.shortcuts import render


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


def list(request):
    allblogs = Blog.objects.all();
    half = int(len(allblogs)/2)
    second = len(allblogs) - half 
    grid1 = [allblogs[x] for x in range(0, half)] 
    grid2 = [allblogs[x] for x in range(half+1, half+second)] 
    return render(request, "Blog/list.html", {
        'grid1': grid1,
        'grid2': grid2,
        'genre': "BLOGS"

    })
