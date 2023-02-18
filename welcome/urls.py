from django.contrib import admin
from django.urls import path, include

from .views import HomePageView, ReviewPageView, EducationPageView, ContactPageView, ConsultationPageView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("review/", ReviewPageView.as_view(), name="review"),
    path("education/", EducationPageView.as_view(), name="education"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("consultation/", ConsultationPageView.as_view(), name="consultation")
]
