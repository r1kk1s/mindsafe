from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Welcome, Diplomas


class WelcomeAdmin(admin.ModelAdmin):
    model = Welcome
    list_display = [
        "title",
        "displayed",
        "get_html_photo"
    ]
    list_display_links = [
        "title",
        "get_html_photo"
    ]
    list_editable = ["displayed"]

    fields = ('title', 'description', 'photo', 'get_html_photo', "displayed")
    readonly_fields = ('get_html_photo',)

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src={object.photo.url} width=50>")
        return "Нет фото"
    
    get_html_photo.short_description = 'Миниатюра'

    


class DiplomasAdmin(admin.ModelAdmin):
    model = Diplomas
    list_display = [
        "title",
        "get_html_photo"
    ]
    list_display_links = [
        "title",
        "get_html_photo",
    ]

    fields = ('title', 'description', 'photo', 'get_html_photo')
    readonly_fields = ('get_html_photo',)

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src={object.photo.url} width=50>")
        return "Нет фото"
    
    get_html_photo.short_description = 'Миниатюра'

    


admin.site.register(Welcome, WelcomeAdmin)

admin.site.register(Diplomas, DiplomasAdmin)
