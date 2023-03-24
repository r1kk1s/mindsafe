import uuid
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models


class AvailableConsultation(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=255, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание услуги")
    photo = models.ImageField(upload_to="photos/cards/%Y/%m/%d/", blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "services"
        verbose_name = "Услугу"
        verbose_name_plural = "Услуги"
        ordering = ["time_created"]
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("consultation_detail", kwargs={"pk":str(self.id)})


class ConsultationEvent(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    consultation = models.ForeignKey(
        AvailableConsultation,
        on_delete=models.CASCADE,
        related_name="consultation",
        verbose_name="Выбранная услуга"
    )
    patient = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="user",
        verbose_name="Пациент"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Опишите вашу проблему (необязательное поле)")
    date_time = models.DateTimeField(verbose_name="Выбирете дату и время")
    approved = models.BooleanField(blank=True, default=False, verbose_name="Одобрить")

    class Meta:
        db_table = "records"
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ["date_time"]

    def __str__(self):
        return self.consultation.title