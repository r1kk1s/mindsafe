from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import ConsultationCards, ConsultationEvent
from .forms import ConsultationEventForm
from welcome.services import get_objects_from_model


def show_available_consultation_list_view(request):
    """Веб-сервис, отображающий доступные консультации"""

    return render(request, "consultations/consultation_list.html",
                  {"consultation_cards": get_objects_from_model(ConsultationCards)})


@login_required
def show_consultation_detail_view(request, pk):
    """Веб-сервис, записывающий текущего пользователя на выбранную консультацию"""
    
    selected_consultation = get_objects_from_model(ConsultationCards, id=pk)[0]

    if request.method == 'POST':
        form = ConsultationEventForm(request.POST)

        if form.is_valid():
            return redirect("my_consultation")
            
    else:
        form = ConsultationEventForm(user=request.user, consultation=selected_consultation)

    context = {
        "form": form,
        "consultation": selected_consultation
    }

    return render(request, "consultations/consultation_detail.html", context)


@login_required
def show_user_consultation_list_view(request):
    """Веб-сервис, отображающий записи текущего пользователя"""
    return render(request,
                  "consultations/my_consultations.html",
                  {"consultations": get_objects_from_model(ConsultationEvent, patient=request.user)})