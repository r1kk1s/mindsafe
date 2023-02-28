from django import template

register = template.Library()


navbar = [
    {"title": "Главная", "view_name": "home"},
    {"title": "Отзывы", "view_name": "review"},
    {"title": "Образование", "view_name": "education"},
    {"title": "Получить консультацию", "view_name": "consultation_list"},
    {"title": "Мои контакты", "view_name": "contact"},
    {"title": "Ваши записи", "view_name": "my_consultations"}
]


@register.simple_tag
def show_navbar_links():
    return navbar