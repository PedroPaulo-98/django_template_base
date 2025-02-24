from django.contrib import admin
from administration.models import CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from administration.forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    fieldsets = (
        ("Personal info", {"fields": ("username", "cpf", "first_name", "last_name", "email", "photo", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "user_permissions")}),
        ("Login information's", {"fields": ("last_login", "date_joined")}),
        ("Group Permissions", {"fields": ("groups",)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'cpf', 'email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    filter_vertical = ('user_permissions',)
    list_display = ('username', 'email', 'cpf', 'first_name', 'last_name', 'is_staff')
    search_fields = ('cpf', 'email', 'first_name', 'last_name')
    ordering = ('cpf',)
    actions = None


admin.site.register(CustomUser, UserAdmin)
