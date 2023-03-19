from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import AvailableConsultation, ConsultationEvent


class AvailableConsultationAdmin(admin.ModelAdmin):
    model = AvailableConsultation
    list_display = [
        "title",
        'get_html_photo',
        "time_created",
    ]
    list_display_links = [
        "title",
        'get_html_photo',
        "time_created",
    ]

    fields = ('title', 'description', 'photo', 'get_html_photo', 'time_created')
    readonly_fields = ('time_created', 'get_html_photo')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src={object.photo.url} width=50>")
        return "Нет фото"
    
    get_html_photo.short_description = 'Миниатюра'



class ConsultationEventAdmin(admin.ModelAdmin):
    model = ConsultationEvent
    list_display = [
        "patient",
        "consultation",
        "date_time",
    ]
    list_display_links = [
        "patient",
        "consultation",
        "date_time",
    ]


admin.site.register(AvailableConsultation, AvailableConsultationAdmin)
admin.site.register(ConsultationEvent, ConsultationEventAdmin)