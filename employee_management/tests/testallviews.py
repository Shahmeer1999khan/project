from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.models import Group
from employee_management.models import Employee
from employee_management.views import *

User = get_user_model()

class ViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='test@example.com', password='testpassword')
        self.manager = User.objects.create_user(username='manager@manager.com', password='testpassword')
        self.managers_group, _ = Group.objects.get_or_create(name='Managers')
        self.manager.groups.add(self.managers_group)

    def test_signup_view(self):
        url = reverse('signup')
        response = self.client.post(url, {'firstname': 'John', 'lastname': 'Doe', 'email': 'john@example.com',
                                          'password': 'testpassword', 'retype_password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  

    def test_signin_view(self):
        url = reverse('signin')
        response = self.client.post(url, {'username': 'test@example.com', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  
        
    def test_list_view(self):
        url = reverse('list')
        request = self.factory.get(url)
        request.user = self.user
        response = list(request)
        self.assertEqual(response.status_code, 200)  
        
    def test_trigger_signal_view(self):
        url = reverse('trigger_signal')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  

    def test_test_view(self):
        url = reverse('test')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  

    def test_manage_view(self):
        url = reverse('manage')
        request = self.factory.get(url)
        request.user = self.manager
        response = manage(request)
        self.assertEqual(response.status_code, 200)  
