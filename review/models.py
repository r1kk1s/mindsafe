from django.contrib.auth import get_user_model
from django.db import models

from consultations.models import AvailableConsultation


class Review(models.Model):
    consultation = models.ForeignKey(
        AvailableConsultation,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Услуга",
    )
    patient = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    review = models.CharField(max_length=255, verbose_name="Отзыв")
    time_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "reviews"
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["time_created"]

    def __str__(self):
        return self.review
    