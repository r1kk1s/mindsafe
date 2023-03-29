from django import template
from django.conf import settings

from apps.consultations.models import ConsultationEvent


register = template.Library()

navbar = [
    {"title": "Главная", "view_name": "home"},
    {"title": "Получить консультацию", "view_name": "consultation_list"},
    {"title": "Отзывы", "view_name": "reviews"},
    {"title": "Мои контакты", "view_name": "contact"},
    {"title": "Ваши записи", "view_name": "my_consultations"},
    {"title": "Статьи", "view_name": "article_list"},
    {"title": "FAQ", "view_name": "issue_list"},
]

@register.simple_tag(takes_context=True)
def show_navbar_links(context):
    """
    Возвращает словарь для навигационной панели
    Для админа заменяет вкладку "Ваши записи"
    """
    request = context["request"]
    if request.user.is_superuser:
        for link in navbar:
            if link["view_name"] == "my_consultations":
                link["title"] = "Записи и вопросы"
                link["view_name"] = "consultations_confirmation"
    return navbar


def get_booked_dates() -> str:
    """Возвращает забронированные даты из БД в строковом формате"""
    dates = []
    for date in ConsultationEvent.objects.values("date_time"):
        dates.append(str(date["date_time"].date()))
    return dates


@register.simple_tag
def get_admin_url() -> str:
    """Возвращает ссылку на админ панель"""
    return settings.ADMIN_URL