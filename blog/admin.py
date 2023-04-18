from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'body', 'categories']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ['posts', 'name', 'body']
