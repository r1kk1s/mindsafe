from django.contrib import admin

from .models import Issue, Answer


admin.site.register(Issue)

admin.site.register(Answer)