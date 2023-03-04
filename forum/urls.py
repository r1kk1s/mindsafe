from django.urls import path, include

from .views import show_issues_list_view, add_issue_view


urlpatterns = [
    path("", show_issues_list_view, name="issue_list"),
    path("add/", add_issue_view, name="add_issue"),
]