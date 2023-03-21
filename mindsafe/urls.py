from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from welcome.views import page_not_found

urlpatterns = [
    # Django admin
    path(settings.ADMIN_URL, admin.site.urls),
    # User manager
    path("accounts/", include("allauth.urls")),
    # Local apps
    path("", include("welcome.urls")),
    path("consultations/", include("consultations.urls")),
    path("review/", include("review.urls")),
    path("articles/", include("articles.urls")),
    path("forum/", include("forum.urls")),
] + static(
 settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


handler404 =    