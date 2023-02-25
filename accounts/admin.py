from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm


CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = [
        "email",
        "username",
        "is_superuser",
    ]
    list_display_links = [
        "email",
        "username",
    ]
    fieldsets = (
        (None, {
            "fields": (("first_name", "last_name"), "email", "contact")
        }),
        ("Логин и пароль", {
            "classes": ("collapse",),
            "fields": ("username", "password"),
        }),
        ("Права доступа", {
            "fields": ("is_staff", "groups",)
        })
    )

admin.site.register(CustomUser, CustomUserAdmin)