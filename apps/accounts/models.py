from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    phone = models.CharField(
        max_length=16,
        blank=True,
        null=True,
        verbose_name="Номер телефона",
    )

    class Meta:
        db_table = "users"
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username