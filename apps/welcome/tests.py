from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Welcome, Diplomas


class WelcomeTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.photo = SimpleUploadedFile(
            name="my_photo.JPG",
            content=open("/home/app/web/staticfiles/images/my_photo.JPG", 'rb').read(),
            content_type='image/jpeg'
        )

        cls.welcome = Welcome.objects.create(
            title="some cool title",
            description="the coolest description",
            photo=cls.photo,
            displayed=True
        )

        cls.diploma = Diplomas.objects.create(
            title="cool diploma",
            description="the best psychologist",
            photo=cls.photo,
        )

        cls.admin_user = get_user_model().objects.create(
            email="test@mail.ru",
            phone="89180123456",
            password="testpass123",
            is_superuser=True
        )

    def test_welcome_model(self):
        self.assertEqual(self.welcome.title, "some cool title")
        self.assertEqual(self.welcome.description, "the coolest description")
        self.assertEqual(self.welcome.displayed, True)

    def test_diploma_model(self):
        self.assertEqual(self.diploma.title, "cool diploma")
        self.assertEqual(self.diploma.description, "the best psychologist")

    def test_show_welcome_page_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "coolest description")
        self.assertContains(response, "cool diploma")
        self.assertTemplateUsed(response, "welcome/home.html")
        self.assertTemplateUsed(response, "welcome/education.html")

    def test_show_my_contact_view(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.admin_user.phone)
        self.assertTemplateUsed(response, "welcome/contact.html")
