from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import StoredPassword
from .encrypt import encrypt_password, decrypt_password

class StoredPasswordTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        
        self.password = StoredPassword.objects.create(
            user=self.user,
            application_name="Facebook",
            username="testuser",
            password="securepassword123",
            description="Social media account password"
        )

    def test_password_creation(self):
        self.assertEqual(self.password.application_name, "Facebook")
        self.assertEqual(self.password.username, "testuser")
        self.assertEqual(str(self.password), "Facebook (testuser)")

class PasswordManagerViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")

    def test_homepage_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_manage_passwords_view(self):
        response = self.client.get(reverse('manage_passwords'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Manage Your Passwords")


class EncryptionUtilsTest(TestCase):
    def test_encryption_and_decryption(self):
        original_password = "mypassword123"
        encrypted = encrypt_password(original_password)
        decrypted = decrypt_password(encrypted)
        self.assertEqual(decrypted, original_password)
        

