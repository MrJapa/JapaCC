from django.test import TestCase
from japa.models import CustomUser, NewCategory, NewRestaurant, NewUnderCategory, NewFood

# Create your tests here.

class CustomUserTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create(username="testuser", password="testpassword", email="testemail")