from django.contrib import admin
from django.urls import path, include

from .views import (show_review_page_view,
                    show_education_page_view,
                    show_welcome_page_view,
                    show_my_contact)


urlpatterns = [
    path("", show_welcome_page_view, name="home"),
    path("review/", show_review_page_view, name="review"),
    path("education/", show_education_page_view, name="education"),
    path("contact/", show_my_contact, name="contact"),
]
