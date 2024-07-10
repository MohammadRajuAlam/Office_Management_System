from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from employeeapp.models import  Department, Employee, EmployeeDetails, Project, Task, Attendance, Account, Salary
from employeeapp.serializers import DepartmentSerializer, EmployeeSerializer, EmployeeDetailsSerializer, ProjectSerializer, TaskSerializer, AttendanceSerializer, AccountSerializer, SalarySerializer

# Here Creating Generics APIViews for all models

# create Department API Views
class DepartmentListCreateAPIView(generics.ListCreateAPIView): # Create Department API for Get all and Post
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    
class DepartmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView): # Create Department API for single Get,put, patch and delete
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    
    # Here writing custome message inside generic if ID doen't exit then show the message
    #???????????????????????????????????????????
    def get_object(self):
          pass
    
# Create Employee API Views
class EmployeeListCreateAPI(generics.ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    
class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    
# Custom API View to get all employees in a department
class DepartmentEmployeesAPIView(APIView):
    
    def get(self, request, pk=None): # Here pk is department id that is primary (auto generated id) in department table
        
        if pk is None:
            return Response({"Response": {"status": 400, "errors": "Please Provide Department ID"}}, status=status.HTTP_400_BAD_REQUEST)
        try:
            department = Department.objects.get(id=pk) # Here id is department id that is primary (auto generated id) in department table
        except Department.DoesNotExist:
            return Response({'Response': {"status": 404, "errors": "Given department ID doesn't Exist."}}, status=status.HTTP_404_NOT_FOUND)
        
        employees = Employee.objects.filter(department=department)
        serializer = EmployeeSerializer(employees, many=True)
        return Response({"response": {"status": 200, "data": serializer.data}}, status=status.HTTP_200_OK) 
        
# Custom API View to get a single employee in a department

class DepartmentSingleEmployeeAPIView(APIView):
    
    def get(self, request, dep_pk=None, empl_pk=None):# Here Having 2 pk one for Department Id like dep_pk, and one for Employee id
        if dep_pk is None or empl_pk is None:
            return Response({'Response': {"status": 400, "errors": "Please Provide Both Department ID and Employee ID"}}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            department = Department.objects.get(id=dep_pk) # Here id is department id that is primary (auto generated id) in department table
        except Department.DoesNotExist:
            return Response({'Response': {"status": 400, "errors": "Given Department ID doesn't Exist."}}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            employee = Employee.objects.get(id=empl_pk, department=department) # Here id is employees id that is primary (auto generated id) in employees table
            serializer = EmployeeSerializer(employee)
            return Response({"response": {"status": 200, "data": serializer.data}}, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({'Response': {"status": 400, "errors": "Given Employee ID doesn't Exist in the specified Department."}}, status=status.HTTP_404_NOT_FOUND)

# Create Employee Details API Views
class EmployeeDetailsListCreateAPIView(generics.ListCreateAPIView):
    queryset=EmployeeDetails.objects.all()
    serializer_class=EmployeeDetailsSerializer
    
class EmployeeDetailsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=EmployeeDetails.objects.all()
    serializer_class=EmployeeDetailsSerializer
    
# Custom API View to get single employeesDetails in a Employeee

class EmployeeSingleDetailsAPIView(APIView):
    def get(self, request, emp_pk=None, emp_detl_pk=None):
        
        if emp_pk is None:
            return Response({"response":{'status':400,"errors":"Please Provide Employee ID"}}, status=status.HTTP_400_BAD_REQUEST)
        try:
            employee=Employee.objects.get(id=emp_pk)
        except Employee.DoesNotExist:
                return Response({"response":{"status":404, "errors":"Employee ID doesn't Exist."}}, status=status.HTTP_404_NOT_FOUND)
            
        if emp_detl_pk is None:
            return Response({"response":{'status':400,"errors":"Please Provide Employee details ID"}}, status=status.HTTP_400_BAD_REQUEST)
        try:
            employeedetails=EmployeeDetails.objects.get(id=emp_detl_pk, employee=employee)
            serializer=EmployeeDetailsSerializer(employeedetails)
            return Response({"response":{"status":200,"data":serializer.data}}, status=status.HTTP_200_OK)
          
        except EmployeeDetails.DoesNotExist:
            return Response({"response":{"status":404,"errors":"Employee Detatails ID doen't Exist"}}, status=status.HTTP_404_NOT_FOUND)

# create project API Views
class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    
class ProjectRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    
# Create Task API Views
class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    
class TaskRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    
# Create Attendance API Views
class AttendanceListCreateAPIView(generics.ListCreateAPIView):
    queryset=Attendance.objects.all()
    serializer_class=AttendanceSerializer
    
class AttendanceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Attendance.objects.all()
    serializer_class=AttendanceSerializer

# Create Account API Views
class AccountListCreateAPIView(generics.ListCreateAPIView):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer
    
class AccountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer
    
class SalaryListCreateAPIView(generics.ListCreateAPIView):
    queryset=Salary.objects.all()
    serializer_class=SalarySerializer
    
class SalaryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer
    
    

    


    
