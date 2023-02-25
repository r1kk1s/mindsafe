from django import forms

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
        
        # widgets = {
        # }
