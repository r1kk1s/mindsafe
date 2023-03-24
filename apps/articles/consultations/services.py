from .models import ConsultationEvent


def get_booked_dates():
    """Возвращает забронированные даты из БД в строковом формате"""

    dates = []
    for date in ConsultationEvent.objects.values("date_time").filter(approved=True):
        dates.append(str(date["date_time"].date()))
    return dates


