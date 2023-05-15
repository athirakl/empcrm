from django.shortcuts import render

# Create your views here.
from api.serializer import EmployeeSerializer
from api.models import Employee
from rest_framework.viewsets import ModelViewSet

class EmployeesView(ModelViewSet):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()