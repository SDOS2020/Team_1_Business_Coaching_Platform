from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CoacheeCreationForm, CoachCreationForm
from .models import CustomUser, Coach, Coachee


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'age', 'is_coach', 'is_coachee']
    fieldsets = UserAdmin.fieldsets + (
        (('Other'), {'fields': ('age', 'is_coach', 'is_coachee')}),
    )

class CoachAdmin(UserAdmin):
    
    add_form = CoachCreationForm
    model = Coach
    list_display = ['username', 'email', 'first_name', 'last_name', 'age', 'is_coach', 'is_coachee']
    fieldsets = UserAdmin.fieldsets + (
        (('Other'), {'fields': ('age', 'is_coach', 'is_coachee')}),
    )


class CoacheeAdmin(UserAdmin):
    
    add_form = CoacheeCreationForm
    model = Coachee
    list_display = ['username', 'email', 'first_name', 'last_name', 'age', 'is_coach', 'is_coachee']
    fieldsets = UserAdmin.fieldsets + (
        (('Other'), {'fields': ('age', 'is_coach', 'is_coachee')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Coach, CoachAdmin)
admin.site.register(Coachee, CoacheeAdmin)
