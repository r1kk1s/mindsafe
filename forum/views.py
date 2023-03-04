from django.shortcuts import render, redirect

from .models import Issue
from .forms import IssueForm


def show_issues_list_view(request):
    return render(request,
                  "forum/issues_list.html",
                  {"issues": Issue.objects.all()})


def add_issue_view(request):
    "Веб-сервис, записывающий проблему пациента в БД"
    
    if request.method == "POST":
        form = IssueForm(request.POST)

        if form.is_valid:
            issue = form.save(commit=False)
            issue.patient = request.user
            form.save()
            return redirect("my_consultations")
    
    form = IssueForm()
    
    return render(request,
                  "forum/add_issue.html",
                  {"form": form})