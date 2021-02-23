from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'author', 'slug',)
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(BlogPost, BlogPostAdmin)
