from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    # User manager
    path("accounts/", include("allauth.urls")),
    # Local apps
    path("", include("welcome.urls")),
    path("consultations/", include("consultations.urls")),
    path("review/", include("review.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
