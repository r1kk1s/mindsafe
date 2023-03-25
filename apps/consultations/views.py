from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required

from .models import AvailableConsultation, ConsultationEvent
from apps.forum.models import Issue
from .forms import ConsultationEventForm


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