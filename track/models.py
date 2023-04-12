from django.db import models

# Create your models here.

class Company(models.Model):
    name=models.CharField(max_length=150)

    def __str__(self):
        return self.name

class employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length = 150)
    designation = models.CharField(max_length = 150)
    join_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name

