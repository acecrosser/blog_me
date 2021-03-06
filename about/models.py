from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    about = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    create = models.DateTimeField(auto_now_add=True)
    mail = models.EmailField(max_length=100, blank=True)
    github = models.CharField(max_length=100, blank=True)
    telegram = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=115)
    avatar = models.ImageField(blank=True, upload_to='../blog/static/images/')
    slug = models.SlugField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
