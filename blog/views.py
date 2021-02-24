from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from .models import BlogPost, BlogRubric


class IndexPage(ListView):

    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    queryset = BlogPost.objects.filter()


class DetailPost(DetailView):

    model = BlogPost
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = BlogPost.objects.all()
        return context


class RubricPage(ListView):

    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self, **kwargs):
        slug = BlogRubric.objects.get(slug=self.kwargs['rubric_slug'])
        return BlogPost.objects.filter(rubric_name=slug.id)

    def get_context_data(self, **kwargs):
        slug = BlogRubric.objects.get(slug=self.kwargs['rubric_slug'])
        context = super().get_context_data(**kwargs)
        context['rubrics'] = BlogRubric.objects.all()
        context['current_rubrics'] = BlogRubric.objects.get(pk=slug.id)
        return context
