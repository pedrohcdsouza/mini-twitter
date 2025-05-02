from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

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