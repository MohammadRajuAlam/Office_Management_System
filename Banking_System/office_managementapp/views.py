from django.shortcuts import render
from office_managementapp.models import Department, Employee, EmployeeDetails, Project, Task, Attendance, Account, Salary
from office_managementapp.serializers import DepartmentSerializer, EmployeeSerializer, EmployeeDetailSerializer, ProjectSerializer, TaskSerializer, AttendanceSerializer, AccountSerializer, SalarySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

##### Here we are creating generics Based view

class DepartmentAPI(generics.ListAPIView, generics.CreateAPIView): # Here access the data, and insert/create/post the data 
    """
    create Department API for access/insert
    """
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    lookup_field='id'
    # Here need custome response
    
class DepartmentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    """
    Create Department API for access/update/delete
    """
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    lookup_field='id'
    
