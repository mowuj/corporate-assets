from rest_framework import serializers
from .models import *

# Serializer for Company Model 
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields = '__all__'

# Serializer for Employee Model 
class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Employee
        fields = '__all__'

# Serializer for Device Model
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Device
        fields = '__all__'

# Serializer for Checkout Model
class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model=Checkout
        fields = '__all__'

# Serializer for Device Log Model
class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLog
        fields = '__all__'
