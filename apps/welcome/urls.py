from django.contrib import admin
from django.urls import path, include

from .views import (show_welcome_page_view,
                    show_my_contact_view)


urlpatterns = [
    path("", show_welcome_page_view, name="home"),
    path("contact/", show_my_contact_view, name="contact"),
]
