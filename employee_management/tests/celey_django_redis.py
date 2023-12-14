from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from employee_management.tasks import test_func
import redis
import json

class CeleryIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_signal_and_celery_integration(self):
        response = self.client.get(reverse('trigger_signal'))
        self.assertEqual(response.status_code, 200)
        