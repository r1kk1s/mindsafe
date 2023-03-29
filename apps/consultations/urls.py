from django.urls import path

from .views import (show_consultation_detail_view,
                    show_available_consultation_list_view,
                    show_user_consultation_list_view,
                    show_issues_and_consultations_for_confirmation_view,
                    confirmed_consultation)


urlpatterns = [
    path("", show_available_consultation_list_view, name="consultation_list"),
    path("<uuid:pk>/", show_consultation_detail_view, name="consultation_detail"),
    path("your_consultations/", show_user_consultation_list_view, name="my_consultations"),
    path("confirmation/", show_issues_and_consultations_for_confirmation_view,
         name="consultations_confirmation"),
    path("confirmation/<uuid:pk>/", confirmed_consultation, name="confirmed_consultation")
]
