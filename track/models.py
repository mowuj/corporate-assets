from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Company(models.Model):
    name=models.CharField(max_length=150)
    users = models.ManyToManyField(User, blank=True)
    def __str__(self):
        return self.name

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length = 150)
    designation = models.CharField(max_length = 150)
    join_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name

class Device(models.Model):
    name=models.CharField(max_length = 150)
    model=models.CharField(max_length = 150)
    company=models.CharField(max_length = 150)
    def __str__(self):
        return self.name
