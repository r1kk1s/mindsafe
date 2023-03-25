from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Review
from apps.consultations.models import AvailableConsultation


class WelcomeTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.photo = SimpleUploadedFile(
            name="my_photo.JPG",
            content=open("/home/app/web/staticfiles/images/my_photo.JPG", 'rb').read(),
            content_type='image/jpeg'
        )

        cls.user = get_user_model().objects.create(
            email="test@mail.ru",
            password="testpass123",
        )

        cls.consultation = AvailableConsultation.objects.create(
            title="some cool consulation",
            description="very cool description",
            photo=cls.photo
        )

        cls.review = Review.objects.create(
            consultation=cls.consultation,
            patient=cls.user,
            review="the cool and fair review",
        )

    def test_review_content(self):
        self.assertEqual(self.review.consultation, self.consultation)
        self.assertEqual(self.review.patient, self.user)
        self.assertEqual(self.review.review, "the cool and fair review")


    def test_show_reviews_view(self):
        response = self.client.get(reverse("reviews"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "fair review")
        self.assertTemplateUsed(response, "review/review_list.html")
