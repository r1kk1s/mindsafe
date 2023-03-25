from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Articles, ArticlesReview


class ArticlesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.photo = SimpleUploadedFile(
            name="my_photo.JPG",
            content=open("/home/app/web/staticfiles/images/my_photo.JPG", 'rb').read(),
            content_type='image/jpeg'
        )

        cls.article = Articles.objects.create(
            title="The best article",
            photo=cls.photo,
            description="the cool story"
        )

        cls.user = get_user_model().objects.create(
            email="test@mail.ru",
            password="testpass123",
        )

        cls.article_review = ArticlesReview.objects.create(
            article=cls.article,
            patient=cls.user,
            review="amazing review"
        )

    def test_article_content(self):
        """Проверяет содержимое созданной статьи"""

        self.assertEqual(self.article.title, "The best article")
        self.assertEqual(self.article.description, "the cool story")

    def test_article_review_content(self):
        """Проверяет содержимое созданного отзыва"""

        self.assertEqual(self.article_review.article, self.article)
        self.assertEqual(self.article_review.patient, self.user)
        self.assertEqual(self.article_review.review, "amazing review")

    def test_show_articles_list_view(self):
        """Проверяет код ответа, отображение описания статьи и используемый шаблон"""

        response = self.client.get(reverse("article_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "cool story")
        self.assertTemplateUsed(response, "articles/article_list.html")

    def test_show_articles_detail_view(self):
        """Проверяет код ответа, отображение описания статьи и отзываи используемый шаблон"""

        response = self.client.get(self.article.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "cool story")
        self.assertContains(response, "amazing review")
        self.assertTemplateUsed(response, "articles/article_detail.html")


