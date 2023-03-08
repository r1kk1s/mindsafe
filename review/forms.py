from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["consultation"].empty_label = "Выберите услугу"

    class Meta:
        model = Review
        fields = (
            "consultation",
            "review",
        )