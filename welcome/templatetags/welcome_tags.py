from django import template

from consultations.models import ConsultationEvent

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


@register.simple_tag
def show_navbar_links():
    return navbar


def get_booked_dates():
    """Возвращает забронированные даты из БД в строковом формате"""
    dates = []
    for date in ConsultationEvent.objects.values("date_time"):
        dates.append(str(date["date_time"].date()))
    return dates