from django.urls import path

from .views import show_articles_list_view, show_articles_detail_view


urlpatterns = [
    path("", show_articles_list_view, name="article_list"),
    path("<uuid:pk>/", show_articles_detail_view, name="article_detail"),
]
