from django.test import TestCase
from django.contrib.auth import get_user_model
  

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create(
            username="robert",
            email="robert@example.com",
            password="testpass123",
            contact="89183331122"
        )
        self.assertEqual(user.username, "robert")
        self.assertEqual(user.email, "robert@example.com")
        self.assertEqual(user.contact, "89183331122")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superadmin",
            email="superadmin@email.com",
            password="testpass123",
            contact="+79180902217"
        )
        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "superadmin@email.com")
        self.assertEqual(admin_user.contact, "+79180902217")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)