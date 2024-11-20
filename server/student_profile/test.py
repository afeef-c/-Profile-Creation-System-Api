from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import StudentProfile

class ProfileCreationTests(TestCase):
    def setUp(self):
        # Set up the test client
        self.client = APIClient()
        self.valid_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "password": "Password123!",
            "phone": "1234567890"
        }
        self.invalid_password_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "password": "pass",
            "phone": "1234567890"
        }
        self.missing_field_data = {
            "email": "john@example.com",
            "password": "Password123!"
        }

    def test_profile_creation_success(self):
        """Test creating a profile with valid data."""
        response = self.client.post('/api/create-profile/', self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("Profile created successfully!", response.data["message"])

    def test_profile_creation_invalid_password(self):
        """Test creating a profile with an invalid password."""
        response = self.client.post('/api/create-profile/', self.invalid_password_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Password must be at least 8 characters long.", response.data["errors"]["password"][0])

    def test_profile_creation_missing_fields(self):
        """Test creating a profile with missing fields."""
        response = self.client.post('/api/create-profile/', self.missing_field_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("This field is required.", response.data["errors"]["name"][0])
