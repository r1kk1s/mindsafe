import datetime
from django import forms
from tempus_dominus.widgets import DateTimePicker

from .services import get_booked_dates
from .models import ConsultationEvent



class ConsultationEventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """При создании формы отображаются забронированные даты из БД и устанавливается формат"""

        super().__init__(*args, **kwargs)
        self.fields["date_time"].input_formats = ['%d/%m/%Y %H:%M']
        self.fields["date_time"].widget = DateTimePicker(
            options={
                "format": "DD/MM/YYYY HH:mm",
                'useCurrent': True,
                'collapse': False,
                "minDate": str(datetime.datetime.today()),
                "disabledDates": get_booked_dates(),
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            },
        )

    class Meta:
        model = ConsultationEvent
        fields = (
            "description",
            "date_time",
        )