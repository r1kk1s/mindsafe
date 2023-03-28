from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Issue, Answer


class ForumTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            email="test@mail.ru",
            password="testpass123",
        )

        cls.issue = Issue.objects.create(
            title="some cool title",
            description="the hardest issue",
            patient=cls.user,
        )

        cls.answer = Answer.objects.create(
            issue=cls.issue,
            description="the best answer",
        )

    def test_issue_model(self):
        self.assertEqual(self.issue.title, "some cool title")
        self.assertEqual(self.issue.description, "the hardest issue")
        self.assertEqual(self.issue.patient, self.user)

    def test_answer_model(self):
        self.assertEqual(self.answer.issue, self.issue)
        self.assertEqual(self.answer.description, "the best answer")

    def test_show_issues_list_view(self):
        response = self.client.get(reverse("issue_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "the hardest issue")
        self.assertContains(response, "the best answer")
        self.assertTemplateUsed(response, "forum/issues_list.html")

    def test_add_issue_view(self):
        self.client.force_login(self.user)
        issue_form_data = {"title": "some title",
                           "description": "some story",
                           "patient": self.user}
        response = self.client.post(reverse("add_issue"),
                                    data=issue_form_data,
                                    follow=True)
        self.assertEqual(response.status_code, 200)

    def test_add_answer_view(self):
        self.user.is_staff = True
        self.user.save()
        self.client.force_login(self.user)
        answer_form_data = {"issue": self.issue,
                            "description": "really helpful answer"}
        response = self.client.post(self.issue.get_absolute_url(),
                                    data=answer_form_data,
                                    follow=True)
        self.assertEqual(response.status_code, 200)