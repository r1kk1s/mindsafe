from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .templatetags.welcome_tags import show_navbar_links


class WelcomeSitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        list_of_links = []
        for nav_item in show_navbar_links():
            list_of_links.append(nav_item["view_name"])
        return list_of_links
    
    def location(self, item):
        return reverse(item)