from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import BlogPost


class IndexPage(ListView):

    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    queryset = BlogPost.objects.filter()

