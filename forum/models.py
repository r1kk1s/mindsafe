from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Issue(models.Model):
    title = models.CharField(unique=True, max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    patient = models.ForeignKey(get_user_model(),
                                on_delete=models.CASCADE,
                                verbose_name="Пациент")
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "issues"
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        ordering = ["time_created",]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("add_answer", kwargs={"pk":str(self.pk)})


class Answer(models.Model):
    issue = models.OneToOneField(Issue,
                                 on_delete=models.CASCADE,
                                 to_field="title",
                                 null=True,
                                 blank=True)
    description = models.TextField(verbose_name="Ответ")
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "answers"
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
        ordering = ["time_created",]
    
    def __str__(self):
        return str(self.issue)