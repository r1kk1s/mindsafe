from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class ReviewSitemap(Sitemap):
    changefreq = "daily"

    def items(self):
        return ["reviews", "add_review"]
    
    def location(self, item):
        return reverse(item)