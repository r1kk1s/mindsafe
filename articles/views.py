from django.shortcuts import render, get_object_or_404

from .models import Articles


def show_articles_list_view(request):
    """Веб-сервис, отображающий список статей"""

    return render(request,
                  "articles/article_list.html",
                  {"articles": Articles.objects.all()})




def show_articles_detail_view(request, pk):
    """Веб-сервис, отображающий выбранную статью"""

    return render(request,
                  "articles/article_detail.html",
                  {"article": get_object_or_404(Articles, pk=pk)})