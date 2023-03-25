from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Django admin
    path(settings.ADMIN_URL, admin.site.urls),
    # User manager
    path("accounts/", include("allauth.urls")),
    # Local apps
    path("", include("apps.welcome.urls")),
    path("consultations/", include("apps.consultations.urls")),
    path("review/", include("apps.review.urls")),
    path("articles/", include("apps.articles.urls")),
    path("forum/", include("apps.forum.urls")),
] + static(
 settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


handler404 = 'apps.welcome.views.page_not_found_view'

handler500 = 'apps.welcome.views.error_500_view'