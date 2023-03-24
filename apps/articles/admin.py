from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Articles, ArticlesReview


class ArticlesReviewAdmin(admin.ModelAdmin):
    model = ArticlesReview
    list_display = [
        "article",
        "patient",
        "time_created",
    ] 
    list_display_links = [
        "article",
        "patient",
        "time_created",
    ]
    
    fields = ("article", "patient", "review", "time_created")
    readonly_fields = ("article", "patient", 'time_created')


class ArticlesAdmin(admin.ModelAdmin):
    model = Articles
    list_display = [
        "title",
        "get_html_photo",
        "time_created",
    ] 
    list_display_links = [
        "title",
        "time_created",
    ]
    
    fields = ('title', 'description', 'photo', 'get_html_photo', 'time_created', 'time_updated')
    readonly_fields = ('time_created', 'time_updated', 'get_html_photo')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src={object.photo.url} width=50>")
        return "Нет фото"
    
    get_html_photo.short_description = 'Миниатюра'


admin.site.register(Articles, ArticlesAdmin)

admin.site.register(ArticlesReview, ArticlesReviewAdmin)