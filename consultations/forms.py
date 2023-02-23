from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from .models import ConsultationEvent


class ConsultationEventForm(forms.ModelForm):

    def __init__(self, user, consultation, *args, **kwargs):
        self.user = user
        self.consultation = consultation
        super().__init__(*args, **kwargs)

    class Meta:
        model = ConsultationEvent
        fields = (
            "description",
            "date",
        )
        
        widgets = {
            "date": AdminDateWidget,
        }


    def save(self, *args, **kwargs):
        """Добавляет в поле patient текущего пользователя,
        а в поле consultation выбранную услугу при записи в таблицу БД"""

        self.instance.patient = self.user
        self.instance.consultation = self.consultation
        return super().save(*args, **kwargs)
