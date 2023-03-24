from django.urls import reverse
from django.test import TestCase
from django.core.files import File
from django.contrib.auth import get_user_model

from .models import Issue, Answer


class ForumTests(TestCase):
    @classmethod
    def setUPTestData(cls):

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

    def test_issue_content(self):
        self.assertEqual(self.issue.title, "some cool title")
        self.assertEqual(self.issue.description, "the hardest issue")
        self.assertEqual(self.issue.patient, self.user)

    def test_answer_content(self):
        self.assertEqual(self.answer.issue, self.issue)
        self.assertEqual(self.answer.description, "the best answer")

    def test_show_issues_list_view(self):
        response = self.client.get(reverse("issue_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "the hardest issue")
        self.assertContains(response, "the best answer")
        self.assertTemplateUsed(response, "forum/issues_list.html")