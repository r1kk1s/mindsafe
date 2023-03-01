from django.contrib import admin

from .models import Welcome, Diplomas


class WelcomeAdmin(admin.ModelAdmin):
    model = Welcome
    list_display = [
        "title",
        "description",
        "photo",
        "displayed",
    ]
    list_display_links = [
        "title",
    ]
    list_editable = ["displayed"]

    


class DiplomasAdmin(admin.ModelAdmin):
    model = Diplomas
    list_display = [
        "title",
        "description",
        "photo", 
    ]
    list_display_links = [
        "title",
    ]

    


admin.site.register(Welcome, WelcomeAdmin)

admin.site.register(Diplomas, DiplomasAdmin)
