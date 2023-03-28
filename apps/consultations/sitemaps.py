from django.contrib.sitemaps import Sitemap

from .models import AvailableConsultation


class ConsultationSitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        return AvailableConsultation.objects.all()
