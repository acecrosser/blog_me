from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from .models import UserProfile
from django.views.generic import ListView, DetailView


class UserProfileDetailPage(DetailView):

    model = UserProfile
    # form_class = RubricForm
    # slug_field = 'author'
    template_name = 'about/about.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super(UserProfileDetailPage, self).get_context_data(**kwargs)
        # context['user'] = User.objects.get()
        context['slug'] = UserProfile.objects.all()
        return context
