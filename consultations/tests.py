import datetime
from django.urls import reverse
from django.test import TestCase
from django.core.files import File
from django.contrib.auth import get_user_model

from .models import AvailableConsultation, ConsultationEvent


class ConsulationTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        file = open("static/images/my_photo.JPG", "rb")
        cls.photo = File(file)

        cls.user = get_user_model().objects.create(
            email="test@mail.ru",
            phone="89181234567",
            password1="testpass123",
            password2="testpass123"
        )

        cls.consultation = AvailableConsultation.objects.create(
            title="some cool consulation",
            description="very cool description",
            photo=cls.photo
        )

        cls.event = ConsultationEvent.objects.create(
            consultation=cls.consultation,
            patient=cls.user,
            description="something interesting",
            date_time=datetime.datetime.today()
        )

    def test_user_content(self):
        self.assertEqual(self.user.email, "test@mail.ru")
        self.assertEqual(self.user.phone, "89181234567")

    def test_consultation_content(self):
        self.assertEqual(self.consultation.title, "some cool consulation")
        self.assertEqual(self.consultation.title, "very cool description")
        self.assertEqual(self.consultation.photo, self.file)

    def test_show_available_consultation_list_view(self):
        response = self.client.get(reverse("consultation_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "cool description")
        self.assertTemplateUsed(response, "consultations/consultation_list.html")

    def test_show_consultation_detail_view_for_logged_in_user(self):
        self.client.login(email="test@mail.ru", password="testpass123")
        response = self.client.get(self.consultation.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "cool description")
        self.assertTemplateUsed(response, "consultations/consultation_detail.html")

    def test_show_user_consultation_list_view(self):
        response = self.client.get(reverse("my_consultations"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "cool consultation")
        self.assertTemplateUsed(response, "consultations/my_consultations.html")

    def test_show_consultation_detail_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(self.consultation.get_absolute_url())
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            "%s?next=/consultation_detail/" % (reverse("account_login"))
        )
        response = self.client.get("%s?next=/books/" % (reverse("account_login")))
        self.assertContains(response, "Вход")