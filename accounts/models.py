from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    contact = models.CharField(max_length=32, blank=True, verbose_name="Контакты")

    class Meta:
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"