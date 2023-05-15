from django.db import models

# Create your models here.
#name,department,salary,adress,phone,email

class Employee(models.Model):
    
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    salary=models.PositiveIntegerField()
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=100)

    def __str__(self):
       return self.name