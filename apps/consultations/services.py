from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import ConsultationEvent


def get_booked_dates():
    """Возвращает забронированные даты из БД в строковом формате"""

    dates = []
    for date in ConsultationEvent.objects.values("date_time").filter(approved=True):
        dates.append(str(date["date_time"].date()))
    return dates


def send_consultation_event_email_for_confirmation(event) -> None:
    """
    Отправляет письмо администратору
    о записи пользователя на выбранную им дату
    """
    context = {"event": event}
    subject = "Запись на прием"
    message = render_to_string(
        "account/email/consultation_for_confirmation_message.txt",
        context
    )

    email = EmailMessage(
        subject=subject,
        body=message,
        to=settings.ADMINS
    )
    email.send()


def send_confirmed_consultation_event_email(event):
    """
    Отправляет письмо пациенту
    после подтверждения его записи администратором
    """
    context = {"event": event}
    subject = "Вы записаны на прием"
    message = render_to_string(
        "account/email/consultation_confirmed_message.txt",
        context
    )

    email = EmailMessage(
        subject=subject,
        body=message,
        to=[event.patient.email]
    )

    email.send()