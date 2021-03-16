from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from pytils.translit import slugify
from .models import UserProfile
from blog.forms import RubricForm
from blog.models import BlogRubric, BlogPost, PostComment, LikeDislike
from django.views.generic import ListView, DetailView, FormView


class UserProfileDetailPage(FormView, DetailView):

    model = UserProfile
    form_class = RubricForm
    template_name = 'about/about.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super(UserProfileDetailPage, self).get_context_data(**kwargs)
        context['rubric_form'] = self.get_form()
        context['comments'] = PostComment.objects.all()
        context['rubric'] = BlogRubric.objects.all()
        context['posts'] = BlogPost.objects.filter(author=1)
        context['slug'] = UserProfile.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        rubric = form.save(commit=False)
        rubric.slug = slugify(rubric)
        rubric.save()
        return super().form_valid(rubric)

    def get_success_url(self):
        return reverse('about:index_about', kwargs={'slug': 'acecrosser'})
