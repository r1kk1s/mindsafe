from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import AvailableConsultation, ConsultationEvent
from apps.forum.models import Issue
from .forms import ConsultationEventForm
from .services import (send_consultation_event_email_for_confirmation,
                       send_confirmed_consultation_event_email)


def show_available_consultation_list_view(request):
    """Веб-сервис, отображающий доступные консультации"""

    return render(request, "consultations/consultation_list.html", {
        "consultation_cards": enumerate(AvailableConsultation.objects.all()),
    })
                  


@login_required
def show_consultation_detail_view(request, pk):
    """Веб-сервис, записывающий текущего пользователя на выбранную консультацию"""
    
    selected_consultation = get_object_or_404(AvailableConsultation, pk=pk)

    if request.method == 'POST':
        form = ConsultationEventForm(request.POST)

        if form.is_valid():
            event = form.save(commit=False)
            event.consultation = selected_consultation
            event.patient = request.user
            event.save()
            send_consultation_event_email_for_confirmation(event)
            return redirect("my_consultations")
            
    else:
        form = ConsultationEventForm()

    context = {
        "form": form,
        "consultation": selected_consultation
    }

    return render(request, "consultations/consultation_detail.html", context)

    
@login_required
def show_user_consultation_list_view(request):
    """Веб-сервис, отображающий записи текущего пользователя"""

    context = {
        "confirmed_consultations": ConsultationEvent.objects.filter(
            patient=request.user, approved=True
        ).select_related("consultation"),
        "non_confirmed_consultations": ConsultationEvent.objects.filter(
            patient=request.user, approved=False
        ).select_related("consultation"),
        "issues": Issue.objects.filter(patient=request.user).select_related("patient", "answer")
    }

    return render(request, "consultations/my_consultations.html", context)


@staff_member_required
def show_issues_and_consultations_for_confirmation_view(request):
    """Веб-сервис, отображающий консультации к подтверждению и вопросы пациентов"""

    context = {
        "non_confirmed_consultations": ConsultationEvent.objects.filter(
            approved=False
        ),
        "confirmed_consultations": ConsultationEvent.objects.filter(
            approved=True
        ),
        "issues": Issue.objects.filter(answer=None)
    }

    return render(request, "consultations/consultations_confirmation.html", context)


@staff_member_required
def confirmed_consultation(request, pk):
    "Подтверждает запись пользователя"

    consultation_event = ConsultationEvent.objects.get(pk=pk)
    consultation_event.approved = True
    consultation_event.save()
    send_confirmed_consultation_event_email(consultation_event)

    return redirect("consultations_confirmation")