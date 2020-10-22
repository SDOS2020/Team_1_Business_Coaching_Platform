from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import CustomUser, Coach, Coachee


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'age', 'is_coach', 'is_coachee']
    fieldsets = UserAdmin.fieldsets + (
        (('Other'), {'fields': ('age', 'is_coach', 'is_coachee')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Coach)
admin.site.register(Coachee)
