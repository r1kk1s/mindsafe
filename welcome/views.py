from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

from .models import Welcome, Diplomas


def show_welcome_page_view(request):
    """Показывает страницу приветствия"""

    return render(request, "welcome/home.html",
                  {"home_info": get_list_or_404(Welcome, displayed=True)[0],
                   "diplomas": Diplomas.objects.all()})


def show_my_contact_view(request):
    """Показывает контакты администратора"""

    return render(request, "welcome/contact.html",
                  {"superuser": get_object_or_404(get_user_model(), is_superuser=True)})


def page_not_found_view(request, exception):
    """Отображает ошибку 404 - страница не найдена"""

    return render(request, "errors/404.html")


def error_500_view(request, exception):
    """Отображет ошибку сервера 500"""

    return render(request, "errors/500.html")