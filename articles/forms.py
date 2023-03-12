from django import forms 

from .models import Articles, ArticlesReview


class ArticlesForm(forms.ModelForm):

    class Meta:
        model = Articles
        fields = (
            "title",
            "photo",
            "description",
        )



class ArticlesReviewForm(forms.ModelForm):

    class Meta:
        model = ArticlesReview
        fields = (
            "review",
        )

