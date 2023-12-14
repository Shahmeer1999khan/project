from django.test import TestCase
from employee_management.models import *
from django.contrib.auth.models import *
from django.utils import timezone
from django.contrib.auth.models import User

class Employeetest(TestCase):
    def test_employee_creation(self):
        department = Department.objects.create(name='Test Department')
        user = User.objects.create_user(username='Mikeee', password='testpass')
        employee = Employee.objects.create(
            user=user,
            first_name='Mike',
            last_name='Alex',
            department=department,
            position='Manager',
            email='Mike_alex@manager.com',
            phone_number='+92147852369',
            hire_date=timezone.now()
        )
        
        
        self.assertEqual(str(employee), 'Mike Alex')
