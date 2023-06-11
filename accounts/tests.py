from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create(username="testuser", email="testuser@gmail.com", password="notagoodpassword")
        self.assertEqual(user.email, "testuser@gmail.com")
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(username="testuser", email="testuser@gmail.com", password="notagoodpassword")
        self.assertEqual(user.email, "testuser@gmail.com")
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)



# Create your tests here.
