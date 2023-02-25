from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm


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
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Номер телефона'})
    )

    class Meta:
        model = get_user_model()