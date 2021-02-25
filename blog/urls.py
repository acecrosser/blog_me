from django.urls import path
from .views import IndexPage, DetailPost, RubricPage, RubricIndexPage

app_name = 'blog'
urlpatterns = [
    path('', IndexPage.as_view(), name='index_page'),
    path('rubrics/', RubricIndexPage.as_view(), name='rub'),
    path('rubrics/<str:rubric_slug>', RubricPage.as_view(), name='rubric'),
    path('rubrics/<str:rubric_slug>/<str:slug>', DetailPost.as_view(), name='detail')
]