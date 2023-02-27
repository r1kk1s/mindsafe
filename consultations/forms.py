from django import forms
from tempus_dominus.widgets import DateTimePicker
from django.core.exceptions import ValidationError

from .models import ConsultationEvent


class ConsultationEventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date_time"].input_formats = ['%d/%m/%Y %H:%M']

    class Meta:
        model = ConsultationEvent
        fields = (
            "description",
            "date_time",
        )
        widgets = {
            "date_time": DateTimePicker(
                options={
                    "format": "DD/MM/YYYY HH:mm",
                    'useCurrent': True,
                    'collapse': False,                    
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                }
            )
        }