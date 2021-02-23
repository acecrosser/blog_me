from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify


class BlogPost(models.Model):

    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    slug = models.SlugField(max_length=255, unique=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    tag = TaggableManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(self, *args, **kwargs)

    class Meta:
        ordering = ('-create', )

    def __str__(self):
        return self.title


class BlogRubric(models.Model):
    pass



