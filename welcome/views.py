from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class HomePageView(TemplateView):
    template_name = "home.html"


class ReviewPageView(TemplateView):
    template_name = "review.html"


class EducationPageView(TemplateView):
    template_name = "education.html"


class ContactPageView(TemplateView):
    template_name = "contact.html"


class ConsultationPageView(TemplateView):
    template_name = "consultation.html"