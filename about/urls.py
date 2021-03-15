from django.urls import path
from .views import UserProfileDetailPage

app_name = 'about'
urlpatterns = [
    path('<str:slug>/', UserProfileDetailPage.as_view(), name='index_about')
]