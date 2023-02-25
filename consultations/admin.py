from django.contrib import admin

from .models import AvailableConsultation, ConsultationEvent


class AvailableConsultationAdmin(admin.ModelAdmin):
    model = AvailableConsultation
    list_display = [
        "title",
        "description",
    ]
    list_display_links = [
        "title",
    ]



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