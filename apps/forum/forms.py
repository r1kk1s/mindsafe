from django import forms 

from .models import Answer, Issue


class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = (
            "description",
        )


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = (
            "description",
        )