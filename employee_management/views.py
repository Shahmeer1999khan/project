from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login as LOGIN
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import Group
from django.db.models import Q
from .tasks import *
from rest_framework import viewsets
from .serializers import *
from django.db.models import Q
from django.http import HttpResponse
from django.http import JsonResponse
from .signals import signal

def trigger_signal(request):
    signal.send(sender=None, custom_data="Hello!")
    return HttpResponse("donneeee")


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

User =get_user_model()
def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email'].casefold()
        password = request.POST['password']
        retype_password = request.POST['retype_password']

        if password == retype_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'A user with this email already exists.')
                return redirect('signup')

            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = firstname
            user.last_name = lastname
            user.save()

            authenticated_user = authenticate(request, username=email, password=password)
            if authenticated_user is not None:
                LOGIN(request, user)

                if '@manager.com' in email: 
                    managers_group, created = Group.objects.get_or_create(name='Managers')
                    user.groups.add(managers_group)
                    messages.success(request, 'You have successfully signed up as a manager!')
                else:
                    messages.success(request, 'You have successfully signed up!')
                return redirect('signin')  
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')

    return render(request, 'registration/signup.html')
@csrf_exempt
def signin(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username'].casefold()
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                LOGIN(request, user)
                return redirect(list)
            else:
                error = "Your account is not active."
        else:
            error = "Incorrect username or password."
        return render(request, 'login.html', {'error': error})
    else:
        return render(request, 'registration/login.html')
        
@login_required
def list(request):
    search = request.GET.get('search', '')
    employees = Employee.objects.all()
    is_manager = request.user.groups.filter(name='Managers').exists()
    if search:
        employees = employees.filter(first_name__icontains = search)
    return render(request,'registration/employee_list.html',{'employees': employees, 'is_manager': is_manager})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request,'registration/employee_list.html', {'employees': employees, 'is_manager': True})


# def delete_employee(request, employee_id):
#     print('ssssssssssssssssssssssssssssssssssssssssssgggggggggggggggggggggggggggggggggggg')
#     employee = get_object_or_404(Employee, id=employee_id)
#     print(employee.first_name)
#     if request.method == 'POST':
#         print('eeeeeeeeeeeeeeeeeee')
#         delete_employee_task.delay(employee_id)
#         return redirect('list')

#     return render(request, 'registration/delete_employee.html', {'employee': employee})


# def perform_add(request):
#     print("aAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
#     result = add.delay(4, 5) 
#     return JsonResponse({'task_id': result.id})

def test(request):
    test_func.delay()
    return HttpResponse("done")

def manage(request):
    employees = Employee.objects.all()
    is_manager = True  
    return render(request, 'registration/employee_list.html', {'employees': employees, 'is_manager': is_manager})

def logout(request):
    return render(request, 'registration/login.html')
