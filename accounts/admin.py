from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *


# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email', 'age', 'is_staff','telegram_id']
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('age','telegram_id',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('age','telegram_id',)}),)


admin.site.register(CustomUser, CustomUserAdmin)
