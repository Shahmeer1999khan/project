from django.test import TestCase , Client
from django.urls import reverse
from employee_management.models import *
from django.utils import timezone
from django.contrib.auth.models import *
from employee_management.models import *



class Employee_view_test(TestCase):
    def setUp(self):
        self.client = Client()
        department =Department.objects.create(name='HR')
        self.employee = Employee.objects.create(
            first_name = 'ALex',
            last_name =' max',
            department=  department,
            position='Manager',
            email='Mike_alex@manager.com',
            phone_number='+92147852369',
            hire_date=timezone.now()
            
        )
        
    def test_employee_list_view(self):
        response = self.client.get(reverse('employee_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.employee.first_name)
