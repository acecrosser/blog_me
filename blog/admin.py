from django.contrib import admin
from .models import BlogPost, BlogRubric, BlogLinks


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'rubric_name', 'author', 'slug',)
    prepopulated_fields = {'slug': ('title', )}


class BlogRubricAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('rubric_name', )}


class BlogLinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'rubric_name')


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogRubric, BlogRubricAdmin)
admin.site.register(BlogLinks, BlogLinksAdmin)
