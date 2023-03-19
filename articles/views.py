from django.shortcuts import render, redirect, get_object_or_404

from .models import Articles, ArticlesReview
from .forms import ArticlesForm, ArticlesReviewForm


def show_articles_list_view(request):
    """Веб-сервис, отображающий список статей"""

    return render(request,
                  "articles/article_list.html",
                  {"articles": Articles.objects.all()})




def show_articles_detail_view(request, pk):
    """Веб-сервис, отображающий выбранную статью"""

    selected_article = get_object_or_404(Articles, pk=pk)

    if request.method == 'POST':
        form = ArticlesReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.article = selected_article
            review.patient = request.user
            review.save()
            return redirect("article_detail", pk)
            
    else:
        form = ArticlesReviewForm()

    context = {
        "form": form,
        "article": selected_article,
        "reviews": ArticlesReview.objects.filter(article=selected_article).select_related("patient")
    }

    return render(request, "articles/article_detail.html", context)


def add_article(request):
    "Веб-сервис, позволяющий администратору писать статьи прямо с сайта"

    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("article_list")
            
    else:
        form = ArticlesForm()

    return render(request, "articles/add_article.html", {"form": form})