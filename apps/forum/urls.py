from django.urls import path

from .views import show_issues_list_view, add_issue_view, add_answer_view


urlpatterns = [
    path("", show_issues_list_view, name="issue_list"),
    path("add/", add_issue_view, name="add_issue"),
    path("answer/<int:pk>/", add_answer_view, name="add_answer"),
]