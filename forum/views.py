from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Issue
from .forms import IssueForm, AnswerForm


def show_issues_list_view(request):
    """Веб-сервис, показывающий список заданных вопросов с ответами на них"""

    return render(request,
                  "forum/issues_list.html",
                  {"issues": Issue.objects.all().select_related("patient", "answer")})


@login_required
def add_issue_view(request):
    """Веб-сервис, записывающий вопрос пациента в БД"""
    
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


def add_answer_view(request, pk):
    """Веб-сервис, записывающий ответ администратора на конкретный вопрос"""

    if request.method == "POST":
        form = AnswerForm(request.POST)

        if form.is_valid:
            issue = form.save(commit=False)
            issue.patient = request.user
            form.save()
            return redirect("issue_list")
    
    form = AnswerForm()
    
    return render(request,
                  "forum/add_answer.html",
                  {"form": form,
                   "issue": get_object_or_404(Issue, pk=pk)})