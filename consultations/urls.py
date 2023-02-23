from django.urls import path

from .views import show_consultation_detail_view, show_available_consultation_list_view, show_user_consultation_list_view


urlpatterns = [
    path("", show_available_consultation_list_view, name="consultation_list"),
    path("<uuid:pk>/", show_consultation_detail_view, name="consultation_detail"),
    path("your_consultations/", show_user_consultation_list_view, name="my_consultations"),
]
