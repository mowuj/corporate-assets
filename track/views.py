
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import generics

# Company Views 
class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

# Employee Views 
class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

# Device View 
class DeviceViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()

# Check out View 
class CheckoutViewSet(viewsets.ModelViewSet):
    serializer_class = CheckoutSerializer
    queryset = Checkout.objects.all()

# Device log View 
class DeviceLogViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceLogSerializer
    queryset = DeviceLog.objects.all()

