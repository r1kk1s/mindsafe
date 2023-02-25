from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from allauth.account.forms import SignupForm
import re



class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CustomSignupForm(SignupForm):

    contact = forms.CharField(
        label="Номер телефона (без пробелов, скобок и дефисов)",
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': '8(900)000-00-00'
        })
    )

    class Meta:
        model = get_user_model()

    def clean_contact(self):
        contact = self.cleaned_data['contact']
        pattern = re.compile(r"^(\+7|8)\d{10}$")
        if not pattern.match(contact):
            raise ValidationError("Номер телефона должен начинаться с '+7' или с '8' и быть не длиннее 10 цифр.")
        self.contact = contact
        return contact

    
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.contact = self.contact
        user.save()
        return user