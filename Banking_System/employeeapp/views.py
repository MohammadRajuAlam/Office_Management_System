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
    
    #???????????????????????????????????????????
    # Here write custome message inside generic if ID doen't exit then show the message
    
# Create Employee API Views
class EmployeeListCreateAPI(generics.ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    
class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    
# Custom API View to get SingleDepartment with all/single employees
class DepartmentEmployeeAPIVie(APIView):
    """
    Department with Employees APIs
    """
    def get(self, request, pk=None, empl_pk=None): 
        
        try:
            department_obj = Department.objects.get(id=pk)
        except Department.DoesNotExist:
            return Response ({"response":{"status":404, "errors":"Department ID doesn't exist."}}, status=status.HTTP_404_NOT_FOUND)
        
        if empl_pk is None:
            employee = Employee.objects.filter(department=department_obj) # Here department is a foreign key field name with department model of Employee model. Note you can check(see) in Employee model
            serializer_class = EmployeeSerializer(employee, many=True)
            return Response ({"response":{"status":200, "payload":serializer_class.data}}, status=status.HTTP_200_OK)
        try:
            employee = Employee.objects.get(id=empl_pk, department=department_obj)
            serializer_class = EmployeeSerializer(employee)
            return Response({"response":{"status":200, "payload":serializer_class.data}}, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({"response":{"status":404, "errors":"Employee ID doesn't exist."}}, status=status.HTTP_404_NOT_FOUND)
        
# Create Employee Details API Views
class EmployeeDetailsListCreateAPIView(generics.ListCreateAPIView):
    queryset=EmployeeDetails.objects.all()
    serializer_class=EmployeeDetailsSerializer
    
class EmployeeDetailsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=EmployeeDetails.objects.all()
    serializer_class=EmployeeDetailsSerializer
    
# Custom API View to get single Employee with Single/all employeesDetails

class EmployeeEmployeeDetailsAPIView(APIView):
    """
    SingleEmploye_SingleEmployeeDetails API
    """
    def get(self, request, pk=None, emp_detl_pk=None):
        
        try:
            employee_obj = Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
                return Response({"response":{"status":404, "errors":"Employee ID doesn't Exist."}}, status=status.HTTP_404_NOT_FOUND)
    
        if emp_detl_pk is None:
            employee_details = EmployeeDetails.objects.filter(employee=employee_obj) # Here employee is a foreign key field name with Employee of Employee Details model
            serializer_class = EmployeeDetailsSerializer(employee_details, many=True) 
            return Response({"response":{"status":200, "payload":serializer_class.data}}, status=status.HTTP_200_OK)
        
        try:
            employee_details = EmployeeDetails.objects.get(id=emp_detl_pk, employee=employee_obj) 
            serializer_class = EmployeeDetailsSerializer(employee_details)
            return Response({"response":{"status":200, "payload":serializer_class.data}}, status=status.HTTP_200_OK) 
        except EmployeeDetails.DoesNotExist:
            return Response({"response":{"status":404, "errors":"Employe Detail ID doesn't exist."}}, status=status.HTTP_404_NOT_FOUND) 
        
# create project API Views
class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    
class ProjectRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    
# Here Created an APIs, Get Single Employee with Single/all Projects
class EmployeeProjectAPIView(APIView):
    """
    Employee with Projects APIs
    """
    def get(self, request, pk=None, pro_pk=None):
        # Retrieve the employee by ID
        try:
            employee_obj = Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            return Response({"response": {"status": 404, "errors": "Employee ID doesn't exist."}}, status=status.HTTP_404_NOT_FOUND)
        
        # Handle Projects
        if pro_pk is None:
            project = Project.objects.filter(employee=employee_obj) # Here employee is a foreign key field name with Employee models of Project models. Note you can see in Project models
            serializer = ProjectSerializer(project, many=True)
            return Response({"response": {"status": 200, "payload": serializer.data}}, status=status.HTTP_200_OK)
        try:
            project = Project.objects.get(id=pro_pk, employee=employee_obj)
            serializer = ProjectSerializer(project)
            return Response({"response": {"status": 200, "payload": serializer.data}}, status=status.HTTP_200_OK)
        except Project.DoesNotExist:
            return Response({"response": {"status": 404, "errors": "Project ID doesn't exist."}}, status=status.HTTP_404_NOT_FOUND)
  
# Create Task API Views
class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    
class TaskRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer

# Here Created Customs APIs for Get Single Employee with Single/all Task
class EmployeeTaskAPIView(APIView):
    """
    Employee with Task APIs
    """
    def get(self, request, pk=None, task_pk=None):
        
        try:
            employee = Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            return Response({"response":{"status":404, "errors":"Employee ID doen't exist."}}, status=status.HTTP_404_NOT_FOUND)
        
        if task_pk is None:
            task = Task.objects.filter(assigned_to=employee) # Here Assigned_to is a foreign key field name with employee models of Task models
            serializer_class = TaskSerializer(task, many=True)
            return Response({"response":{"status":200, "payload": serializer_class.data}}, status=status.HTTP_200_OK)
        
        try:
            task = Task.objects.get(id=task_pk, assigned=employee) 
            serializer_class = TaskSerializer(task)
            return Response({"response":{"status":200, "payload":serializer_class.data}}, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"response":{"status":404, "errors":"Task ID doen't exist."}}, status=status.HTTP_404_NOT_FOUND)
            
# Create Attendance API Views
class AttendanceListCreateAPIView(generics.ListCreateAPIView):
    queryset=Attendance.objects.all()
    serializer_class=AttendanceSerializer
    
class AttendanceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Attendance.objects.all()
    serializer_class=AttendanceSerializer
    
# Here Created customs API to Get a specific Employee with single/all Attendance
class EmployeeAttendanceAPIView(APIView):
    """
    Employee with Attendance APIs
    """ 
    def get(self, request, pk=None, attend_pk=None):
        try:
            employee_obj = Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            return Response({"response":{"status":404, "errors":"Employee ID doesn't exist."}}, status=status.HTTP_404_NOT_FOUND)
        
        if attend_pk is None:
            attendance_obj = Attendance.objects.filter(employee=employee_obj) # Here employee is a foreign key field name with Employee models of Attendance model 
            serializer_class = AttendanceSerializer(attendance_obj, many=True)
            return Response({"response":{"status":200, "payload":serializer_class.data}}, status=status.HTTP_200_OK)
    
        try:
            attendance_obj = Attendance.objects.get(id=attend_pk, employee=employee_obj)
            serializer_class = AttendanceSerializer(attendance_obj)
            return Response({"response":{"status":200, "payload":serializer_class.data}}, status=status.HTTP_200_OK)
        except Attendance.DoesNotExist:
            return Response({"response":{"status":404, "errors":"Attendance ID doen't exist."}}, status=status.HTTP_404_NOT_FOUND)
        
# Create Account API Views
class AccountListCreateAPIView(generics.ListCreateAPIView):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer
    
class AccountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer
    
# Here Created customs API to Get a specific Employee with single/all Account
class EmployeeAccountAPIView(APIView):
    """
    Employee with Account APIs
    """
    def get(self, request, pk=None, acc_pk=None):
        
        try:
            employee_obj = Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            return Response({"response":{"status":404, "errors":"Employee ID doen't exist."}}, status=status.HTTP_404_NOT_FOUND)
        
        if acc_pk is None:
            account_obj = Account.objects.filter(employee=employee_obj) # Here employee is a foreign key field name with Employee models of Account model 
            serializer_class = AccountSerializer(account_obj, many=True)
            return Response({"response":{"status":200, "payload":serializer_class.data}}, status=status.HTTP_200_OK)
        
        try:
            account_obj = Account.objects.get(id=acc_pk, employee=employee_obj)
            serializer_class = AccountSerializer(account_obj)
            return Response({"response":{"status":200, "payload":serializer_class.data}}, status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            return Response({"response":{"status":404, "errors":"Account ID doen't exist."}}, status=status.HTTP_404_NOT_FOUND)
        
class SalaryListCreateAPIView(generics.ListCreateAPIView):
    queryset=Salary.objects.all()
    serializer_class=SalarySerializer
    
class SalaryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer
    
# Here Created customs API to Get a specific Employee with single/all Salary
class EmployeeSalaryAPIView(APIView):
    """
    Employee with Salary APIs
    """
    def get(self, request, pk=None, sal_pk=None):
        try:
            employee_object = Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            return Response({"response": {"status": 404, "errors": "Employee ID doesn't exist."}}, status=status.HTTP_404_NOT_FOUND)
        
        if sal_pk is None:
            salary_objects = Salary.objects.filter(employee=employee_object)
            serializer = SalarySerializer(salary_objects, many=True)
            return Response({"response": {"status": 200, "payload": serializer.data}}, status=status.HTTP_200_OK)
        
        try:
            salary_object = Salary.objects.get(id=sal_pk, employee=employee_object)
            serializer = SalarySerializer(salary_object)
            return Response({"response": {"status": 200, "payload": serializer.data}}, status=status.HTTP_200_OK)
        except Salary.DoesNotExist:
            return Response({"response": {"status": 404, "errors": "Salary ID doesn't exist."}}, status=status.HTTP_404_NOT_FOUND)