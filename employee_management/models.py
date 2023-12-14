from django.db import models
from django.contrib.auth.models import User, Group

class Department(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name}"

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    hire_date = models.DateField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
managers_group, created = Group.objects.get_or_create(name='Managers')

     