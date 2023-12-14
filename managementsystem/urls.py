from django.contrib import admin
from django.urls import path, include
from employee_management.views import *
from django.conf import settings
from rest_framework.routers import DefaultRouter
from .consumers import MyConsumer

admin.autodiscover()

router = DefaultRouter()
router.register(r'employee',EmployeeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('',signin, name='signin'),
    path('signup/',signup, name='signup'),
    path('employee/', list, name='list'),  
    path('manage/',manage, name='manage'),
    path('logout/',logout, name='logout'),
    path('emp_list/',employee_list, name='employee_list'),
    # path('delete/<int:employee_id>/', delete_employee, name='delete_employee'),
    path('perform_add/', test, name='test'),
    path('trigger-signal/', trigger_signal, name='trigger_signal'),
    path("ws/hello/", MyConsumer.as_asgi()),
    # path('accounts/login/', LoginView.as_view(), name='login'),    
    
    
]
