from django.contrib import admin

from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'slug', 'author', 'body', 'publish', 'created', 'updated', 'status']
    search_fields = ['title', 'content']

admin.site.register(Post, PostAdmin)
