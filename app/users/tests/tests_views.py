from rest_framework.test import APITestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model

from ..views import authentication

User = get_user_model()


class ViewsTests(APITestCase):

    def test_authentication_view(self):
        view = resolve(reverse('users:register'))
        self.assertIs(view.func.view_class, authentication.RegisterView)