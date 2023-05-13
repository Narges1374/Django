from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'categories']
    fields = ['title', 'author', 'categories', 'body', 'slug']
    search_fields = ['title', 'author__username']
    list_per_page = 10


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ['posts', 'name', 'body']
