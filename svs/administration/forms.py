from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "cpf", "email", "first_name", "last_name")


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ("cpf", "password")


class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = ("username", "cpf", "email", "first_name", "last_name", "is_active", "is_staff", "is_superuser", "groups", "user_permissions", "password")
