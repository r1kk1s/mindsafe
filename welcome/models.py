from django.db import models


class Welcome(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to="photos/me/%Y/%m/%d/", verbose_name="Фото")

    class Meta:
        verbose_name = "домашнюю страницу"
        verbose_name_plural = "Домашняя страница"



class Diplomas(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to="photos/diplomas/%Y/%m/%d/", verbose_name="Фото")

    class Meta:
        verbose_name = "Диплом"
        verbose_name_plural = "Дипломы"