from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .models import LikeDislike, BlogPost, PostComment
from .views import IndexPage, DetailPost, RubricPage, RubricIndexPage, TagPosts, VoteView
from .views import add_post, edit_post

app_name = 'blog'
urlpatterns = [
    path('', IndexPage.as_view(), name='index_page'),
    path('add/', add_post, name='add_post'),
    path('edit/<str:slug>', edit_post, name='edit_post'),
    path('rubrics/', RubricIndexPage.as_view(), name='rub'),
    path('tags/<str:tag_slug>', TagPosts.as_view(), name='tags'),
    path('rubrics/<str:rubric_slug>', RubricPage.as_view(), name='rubric'),
    path('rubrics/<str:rubric_slug>/<str:slug>', DetailPost.as_view(), name='detail'),
]
