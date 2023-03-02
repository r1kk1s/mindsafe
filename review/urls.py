from django.urls import path

from .views import show_reviews_view, add_review_view

urlpatterns = [
    path("", show_reviews_view, name="reviews"),
    path("add/", add_review_view, name="add_review"),
]
