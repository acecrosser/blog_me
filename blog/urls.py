from django.urls import path
from .views import IndexPage, DetailPost, RubricPage

app_name = 'blog'
urlpatterns = [
    path('', IndexPage.as_view(), name='index_page'),
    path('<str:rubric_slug>', RubricPage.as_view(), name='rubric'),
    path('<str:rubric_slug>/<str:slug>', DetailPost.as_view(), name='detail')
]