from django.contrib.sitemaps import Sitemap

from .models import Issue


class IssueSitemap(Sitemap):
    changefreq = "daily"

    def items(self):
        return Issue.objects.all()