from rest_framework import serializers
from .models import *

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source='company.name')
    class Meta:
        model=Employee
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Device
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Device
        fields = '__all__'


class CheckoutSerializer(serializers.ModelSerializer):
    device = serializers.CharField(source='device.name')
    employee = serializers.CharField(source='employee.name')
    class Meta:
        model=Checkout
        fields = '__all__'


