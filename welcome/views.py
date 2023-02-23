from django.shortcuts import render
from django.contrib.auth import get_user_model

from .models import Welcome, Diplomas
from .services import get_objects_from_model 



def show_welcome_page_view(request):
    """Показывает страницу приветствия"""

    return render(request, "welcome/home.html",
                  {"home_info": get_objects_from_model(Welcome)})


def show_education_page_view(request):
    """Показывает страницу с дипломами"""

    return render(request, "welcome/education.html",
                  {"diplomas": get_objects_from_model(Diplomas)})


def show_review_page_view(request):
    """Показывает страницу с отзывами"""

    return render(request, "review.html")


def show_my_contact(request):
    """Показывает контакты администратора"""

    return render(request, "welcome/contact.html",
                  {"superuser": get_objects_from_model(get_user_model(), is_superuser=True)})