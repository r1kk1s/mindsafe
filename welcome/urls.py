from django.contrib import admin
from django.urls import path, include

from .views import (show_education_page_view,
                    show_welcome_page_view,
                    show_my_contact)


urlpatterns = [
    path("", show_welcome_page_view, name="home"),
    path("education/", show_education_page_view, name="education"),
    path("contact/", show_my_contact, name="contact"),
]
