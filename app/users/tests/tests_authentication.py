from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthenticationTests(APITestCase):

    def test_users_can_register(self):
        url = reverse('users:register')
        data = {
            'username': 'testuser2',
            'email': 'teste@example.com2',
            'password': 'testpassword'
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='testuser').exists())