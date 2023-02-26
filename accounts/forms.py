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

    phone = forms.CharField(
        label="Номер телефона (без пробелов, скобок и дефисов)",
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': '8(900)000-00-00'
        })
    )

    class Meta:
        model = get_user_model()

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        pattern = re.compile(r"^(\+7|8)\d{10}$")
        if not pattern.match(phone):
            raise ValidationError("Номер телефона должен начинаться с '+7' или с '8' и быть не длиннее 10 цифр.")
        self.phone = phone
        return phone
    
    def save(self, request):
        """
        В документации django-allauth при добавлении в форму пользовательских полей
        необходимо явно присваивать этим полям значение
        """
        
        user = super(CustomSignupForm, self).save(request)
        user.phone = self.phone
        user.save()
        return user