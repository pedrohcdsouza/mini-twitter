from rest_framework.test import APITestCase
from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework import status
from django.contrib.auth import get_user_model

from .views import authentication

User = get_user_model()

class UsersURLTests(TestCase):

    def test_users_register_url_is_correct(self):
        url = reverse('users:register')
        self.assertEqual(url, '/api/users/register/')

    def test_users_login_url_is_correct(self):
        url = reverse('users:login')
        self.assertEqual(url, '/api/users/login/')

    def test_users_refresh_url_is_correct(self):
        url = reverse('users:refresh')
        self.assertEqual(url, '/api/users/login/refresh/')

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
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_user_can_login(self):
        url = reverse('users:login')
        data = {  
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(url, data)

        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

class ViewsTests(APITestCase):

    def test_authentication_view(self):
        view = resolve(reverse('users:register'))
        self.assertIs(view.func.view_class, authentication.RegisterView)