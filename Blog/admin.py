from django.contrib import admin
from .models import Blog, Comment, Author
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.

admin.site.register(Blog, MarkdownxModelAdmin)
admin.site.register(Comment)
admin.site.register(Author)
