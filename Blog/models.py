from django.db import models
from django.urls import reverse
# Create your models here.
from markdownx.models import MarkdownxField

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    authorimage = models.ImageField(default='profile.png')
    content = MarkdownxField()
    image = models.ImageField(default='neofetch.jpg')
    genre = models.CharField(max_length=40)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('read', args=[str(self.id)])
