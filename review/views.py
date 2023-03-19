from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Review
from .forms import ReviewForm


def show_reviews_view(request):
    """Веб-сервис, отображающий все отзывы"""

    return render(request,
                  "review/review_list.html",
                  {"reviews": enumerate(Review.objects.all().select_related("consultation", "patient"))})


@login_required
def add_review_view(request):
    """Веб-сервис, позволяющий добавить отзыв о консультации"""

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.patient = request.user
            review.save()
            return redirect("reviews")
            
    else:
        form = ReviewForm()
    return render(request, "review/add_review.html", {"form": form})
