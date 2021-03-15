from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('author', 'about', 'status', 'mail', 'create')


admin.site.register(UserProfile, UserProfileAdmin)
