from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('categories', views.categories, name="categories"),
    path('<int:num>', views.read, name="read"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('list', views.list, name="list")
]
