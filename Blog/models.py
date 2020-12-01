from django.db import models
from django.urls import reverse
# Create your models here.
from markdownx.models import MarkdownxField


class Author(models.Model):
    authorName = models.CharField(max_length=20)
    authorUsername = models.CharField(max_length=20, primary_key=True)
    authorImage = models.ImageField(default='profile.png')
    authorBio = models.TextField(max_length=250)
    authorTwitter = models.CharField(max_length=100, blank=True)
    authorInsta = models.CharField(max_length=100, blank=True)
    authorFacebook = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.authorUsername}"


class Blog(models.Model):
    Genre_Choices = (
        ("Anime", "Anime"),
        ("Movies", "Movies"),
        ("Series", "Series"), 
        ("Novels", "Novels"),
        ("Sports", "Sports"),
        ("Poetry", "Poetry"),

    )

    Post_Mode = (
        ("Draft", "Draft"),
        ("Published", "Published"),
    )
    title = models.CharField(max_length=85, unique=True)
    subheading = models.CharField(max_length=140)
    authorUsername = models.ForeignKey(Author, default='anonymous', on_delete=models.SET_DEFAULT)
    content = MarkdownxField()
    image = models.ImageField(default='neofetch.jpg')
    genre = models.CharField(max_length=40, choices=Genre_Choices)
    likes = models.IntegerField(default=0)
    mode = models.CharField(max_length=10,choices=Post_Mode,default="Draft")
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('read', args=[str(self.id)])


class Comment(models.Model):
    # replyID is the ID of the  comment  to which the user has replied to
    replyID = models.IntegerField(default=None)
    Post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    Username = models.CharField(max_length=20)
    commentContent = models.TextField(max_length=350)
    commentlikes = models.IntegerField(default=0)
    approved = models.BooleanField(default=True)
    
    def approve(self):
        self.approved = True
        self.save()

    def disapprove(self):
        self.approved = False
        self.save()
