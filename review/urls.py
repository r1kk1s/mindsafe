from django.urls import path

from .views import show_reviews, add_review

urlpatterns = [
    path("", show_reviews, name="reviews"),
    path("add/", add_review, name="add_review"),
]
