from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    about = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    create = models.DateTimeField(auto_now_add=True)
    mail = models.EmailField(max_length=100)
    status = models.CharField(max_length=115)
    avatar = models.ImageField(blank=True)
    slug = models.SlugField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
