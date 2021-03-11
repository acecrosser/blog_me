from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.db.models import Sum
from taggit.managers import TaggableManager
from pytils.translit import slugify


class BlogPost(models.Model):

    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    rubric_name = models.ForeignKey('BlogRubric', on_delete=models.CASCADE, related_name='post')
    slug = models.SlugField(max_length=255, unique=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    votes = GenericRelation('LikeDislike', related_name='blogpost')

    class Meta:
        ordering = ('-create', )
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class BlogRubric(models.Model):

    rubric_name = models.CharField(max_length=150, db_index=True, verbose_name='Рубрика')
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.rubric_name

    class Meta:
        ordering = ('rubric_name', )
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()
    location = models.CharField(max_length=30, blank=True)


class PostComment(models.Model):

    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comment')
    comment = models.TextField()
    author = models.CharField(max_length=50)
    create = models.DateTimeField(auto_now_add=True)
    votes = GenericRelation('LikeDislike', related_name='post_comment')


class LikeDislikeManager(models.Manager):

    use_for_related_fields = True

    def likes(self):
        return self.get_queryset().filter(vote__gt=0)

    def dislikes(self):
        return self.get_queryset().filter(vote__lt=0)

    def sum_rating(self):
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0

    def blogpost(self):
        return self.get_queryset().filter(content_type__model='blogpost').order_by('-blogpost')

    def post_comment(self):
        return self.get_queryset().filter(content_type__model='post_comment').order_by('-post_comment')


class LikeDislike(models.Model):

    LIKE = 1
    DISLIKE = -1

    VOTES = {
        (LIKE, 'Нравится'),
        (DISLIKE, 'Не нравится')
    }

    vote = models.SmallIntegerField(verbose_name='Голос', choices=VOTES)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = LikeDislikeManager()
