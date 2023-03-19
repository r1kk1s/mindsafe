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
            "classes": ("wide",),
            "fields": ("username", "password",
                       ("first_name", "last_name"),
                       "email", "phone")
        }),
        
        ("Права доступа", {
            "classes": ("collapse",),
            "fields": ("is_staff", "groups",)
        }),
        ("Важные даты", {
            "classes": ("wide",),
            "fields": ("last_login", "date_joined")
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)