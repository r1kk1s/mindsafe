from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import AvailableConsultation, ConsultationEvent


class ConsulationTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.photo = SimpleUploadedFile(
            name="my_photo.JPG",
            content=open("/home/app/web/staticfiles/images/my_photo.JPG", 'rb').read(),
            content_type='image/jpeg'
        )

        cls.user = get_user_model().objects.create(
            email="test@mail.ru",
            phone="89181234567",
            password="testpass123",
        )
        cls.user.is_active = True
        cls.user.save()

        cls.consultation = AvailableConsultation.objects.create(
            title="some cool consulation",
            description="very cool description",
            photo=cls.photo
        )

        cls.event = ConsultationEvent.objects.create(
            consultation=cls.consultation,
            patient=cls.user,
            description="something interesting",
            date_time=timezone.now()
        )

    def test_user_model(self):
        self.assertEqual(self.user.email, "test@mail.ru")
        self.assertEqual(self.user.phone, "89181234567")

    def test_available_consultation_model(self):
        self.assertEqual(self.consultation.title, "some cool consulation")
        self.assertEqual(self.consultation.description, "very cool description")

    def test_consultation_event_model(self):
        self.assertEqual(self.event.consultation, self.consultation)
        self.assertEqual(self.event.patient, self.user)
        self.assertEqual(self.event.description, "something interesting")

    def test_show_available_consultation_list_view(self):
        response = self.client.get(reverse("consultation_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "cool description")
        self.assertTemplateUsed(response, "consultations/consultation_list.html")

    def test_show_consultation_detail_view_for_logged_in_user(self):
        self.client.force_login(self.user)
        response = self.client.get(self.consultation.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "cool description")
        self.assertTemplateUsed(response, "consultations/consultation_detail.html")
        consultation_event_form_data = {"consultation": self.consultation,
                                        "patient": self.user,
                                        "description": "some story",
                                        "date_time": timezone.now()}
        response = self.client.post(self.consultation.get_absolute_url(),
                                    data=consultation_event_form_data,
                                    follow=True)
        self.assertEqual(response.status_code, 200)

    def test_show_user_consultation_list_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("my_consultations"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "consultations/my_consultations.html")

    def test_show_consultation_detail_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(self.consultation.get_absolute_url())
        self.assertEqual(response.status_code, 302)