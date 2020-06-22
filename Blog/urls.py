from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('categories', views.categories, name="categories"),
    path('<int:num>', views.read, name="read"),

]
