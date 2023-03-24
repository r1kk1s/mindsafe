from django.urls import reverse
from django.test import TestCase
from django.core.files import File
from django.contrib.auth import get_user_model

from .models import Welcome, Diplomas


class WelcomeTests(TestCase):
    @classmethod
    def setUPTestData(cls):
        file = open("/static/images/my_photo.JPG", "rb")
        cls.photo = File(file)
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

    def test_welcome_content(self):
        self.assertEqual(self.welcome.title, "some cool title")
        self.assertEqual(self.welcome.description, "the coolest description")
        self.assertEqual(self.welcome.photo, self.photo)
        self.assertEqual(self.welcome.displayed, True)

    def test_diploma_content(self):
        self.assertEqual(self.diploma.title, "cool diploma")
        self.assertEqual(self.diploma.description, "best psychologist")
        self.assertEqual(self.diploma.photo, self.photo)

    def test_show_welcome_page_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "coolest description")
        self.assertContains(response, "cool diploma")
        self.assertTemplateUsed(response, "welcome/home.html")
        self.assertTemplateUsed(response, "welcome/education.html")

    def test_show_my_contact_view(self):
        admin = get_user_model().objects.get(is_superuser=True)
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, admin.phone)
        self.assertTemplateUsed(response, "welcome/contact.html")
