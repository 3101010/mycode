from django.contrib import admin

# Register your models here.
# from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from mainapp.models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    verbose_name = 'UserProfile'
    max_num = 1

class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline, ]

admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)