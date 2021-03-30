from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .models import LikeDislike, BlogPost, PostComment
from .views import IndexPage, DetailPost, RubricPage, RubricIndexPage, TagPosts, VoteView
from .views import add_post, edit_post

from django.contrib.sessions import middleware

app_name = 'ajax'
urlpatterns = [
    url(r'^blogpost/(?P<pk>\d+)/like/$', VoteView.as_view(model=BlogPost, vote_type=LikeDislike.LIKE),
        name='blogpost_like'),
    url(r'^blogpost/(?P<pk>\d+)/dislike/$', VoteView.as_view(model=BlogPost, vote_type=LikeDislike.DISLIKE),
        name='blogpost_dislike'),
    url(r'^postcomment/(?P<pk>\d+)/like/$', login_required(VoteView.as_view(model=PostComment, vote_type=LikeDislike.LIKE)),
        name='blogpost_like'),
    url(r'^postcomment/(?P<pk>\d+)/dislike/$', login_required(VoteView.as_view(model=PostComment, vote_type=LikeDislike.DISLIKE)),
        name='blogpost_dislike')

]
