from django.contrib.sitemaps import Sitemap

from .models import Articles


class ArticleSitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        return Articles.objects.all()
