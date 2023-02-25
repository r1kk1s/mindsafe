from django.shortcuts import render, get_list_or_404
from django.contrib.auth import get_user_model

from .models import Welcome, Diplomas


def show_welcome_page_view(request):
    """Показывает страницу приветствия"""
    
    return render(request, "welcome/home.html",
                  {"home_info": get_list_or_404(Welcome)[0]})


def show_education_page_view(request):
    """Показывает страницу с дипломами"""

    return render(request, "welcome/education.html",
                  {"diplomas": Diplomas.objects.all()})
                  # {"diplomas": get_list_or_404(Diplomas)})


def show_review_page_view(request):
    """Показывает страницу с отзывами"""

    return render(request, "review.html")


def show_my_contact(request):
    """Показывает контакты администратора"""

    return render(request, "welcome/contact.html",
                  {"superuser": get_list_or_404(get_user_model(), is_superuser=True)})