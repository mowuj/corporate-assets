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
    

