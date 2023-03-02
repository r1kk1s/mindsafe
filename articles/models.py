import uuid
from django.db import models
from django.urls import reverse



class Articles(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=255, verbose_name="Название")
    photo = models.ImageField(upload_to="photos/articles/%Y/%m/%d/", verbose_name="Картинка")
    description = models.TextField(verbose_name="Содержание")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_updated = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    class Meta:
        db_table = "articles"
        verbose_name = "Статью"
        verbose_name_plural = "Статьи"
        ordering = ["time_created", "time_updated"]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk":str(self.id)})
