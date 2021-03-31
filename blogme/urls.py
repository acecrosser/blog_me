from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import RedirectView

urlpatterns = [
    path('', include('blog.urls'), name='blog'),
    path('api/', include('blog.urls_api'), name='api'),
    path('about/', include('about.urls'), name='about'),
    path('captcha/', include('captcha.urls')),
    path('admin/', admin.site.urls),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
]
