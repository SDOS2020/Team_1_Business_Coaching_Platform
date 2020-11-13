from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm , CoacheeCreationForm, CoachCreationForm
from .models import CustomUser, Coach, Coachee, Connection


class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('email', 'age', 'is_coach', 'is_coachee', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('age', 'is_coach', 'is_coachee')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class CoachAdmin(admin.ModelAdmin):
    add_form = CoachCreationForm
    model = Coach
    list_display = ['user','first_name', 'last_name']


class CoacheeAdmin(admin.ModelAdmin):
    add_form = CoacheeCreationForm
    model = Coachee
    list_display = ['user','first_name', 'last_name']


class ConnectionAdmin(admin.ModelAdmin):
    model = Connection
    list_display = ['coach','coachee', 'accepted']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Coach, CoachAdmin)
admin.site.register(Coachee, CoacheeAdmin)
admin.site.register(Connection, ConnectionAdmin)
