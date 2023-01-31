from django.test import TestCase
from django.contrib.auth.models import User


class AuthenticationTestCase(TestCase):
    """
    Simple authentication test
    """

    def setUp(self):
        User.objects.create(username='testuser')

    def test_user_created(self):
        user = User.objects.filter(username='testuser')
        self.assertTrue(user.exists())
