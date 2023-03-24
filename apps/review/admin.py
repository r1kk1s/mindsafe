from django.contrib import admin

from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = [
        "consultation",
        "patient",
        "time_created",
    ]
    list_display_links = [
        "consultation",
        "patient",
        "time_created",
    ]

    fields = ("consultation", "patient", "review", "time_created")
    readonly_fields = ("consultation", "patient", "time_created")


admin.site.register(Review, ReviewAdmin)