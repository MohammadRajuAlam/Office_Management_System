from django.contrib import admin
from django.urls import path
from employeeapp.views import (
    DepartmentListCreateAPIView,
    DepartmentRetrieveUpdateDestroyAPIView,
    EmployeeListCreateAPI,
    EmployeeRetrieveUpdateDestroyAPIView,
    DepartmentEmployeesAPIView,
    DepartmentSingleEmployeeAPIView,
    EmployeeDetailsListCreateAPIView,
    EmployeeSingleDetailsAPIView,
    EmployeeDetailsRetrieveUpdateDestroyAPIView,
    ProjectListCreateAPIView,
    ProjectRetrieveUpdateAPIView,
    TaskListCreateAPIView,
    TaskRetrieveUpdateAPIView,
    AttendanceListCreateAPIView,
    AttendanceRetrieveUpdateDestroyAPIView,
    AccountListCreateAPIView,
    AccountRetrieveUpdateDestroyAPIView,
    SalaryListCreateAPIView,
    SalaryRetrieveUpdateDestroyAPIView)


urlpatterns = [
    
    # Create Department URLs
    path('departments/', DepartmentListCreateAPIView.as_view(), name='Department-list-create'),
    path('departments/<int:pk>/', DepartmentRetrieveUpdateDestroyAPIView.as_view(), name='Department-details'),
    
    # Create Employee URLs
    path('employees/', EmployeeListCreateAPI.as_view(), name='Employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='Employee-details'),
    
    # Custom URL to get all employees of a specific department like department/1/employees # Here access all employees of department/1
    path('departments/<int:pk>/employees/', DepartmentEmployeesAPIView.as_view(), name='Department-Employee'),
    
    # Custom URL to get single employees of a specific department like department/1/employees/1 # Here access single employees of department/1
    path('departments/<int:dep_pk>/employees/<int:empl_pk>/', DepartmentSingleEmployeeAPIView.as_view(), name='Department-Single-Employee'),
    
    # Create Employee Details URLs
    path('employeeDetails/', EmployeeDetailsListCreateAPIView.as_view(), name='EmployeeDetails-list-create'),
    path('employeeDetails/<int:pk>/', EmployeeDetailsRetrieveUpdateDestroyAPIView.as_view(), name='EmployeeDetails-Details'),
    
    # Custome URLs to get single EmployeeDetails of a specific Employee
    path("employees/<int:emp_pk>/employeedetails/<int:emp_detl_pk>/", EmployeeSingleDetailsAPIView.as_view(), name='Employee-EmployeeDetails'),
    
    # Create project URLs
    path('project/', ProjectListCreateAPIView.as_view(), name='Project-list-create'),
    path('project/<int:pk>/',ProjectRetrieveUpdateAPIView.as_view(), name='Project-details'),
    
    # Custome API URLS
    
    # Create Task URLs
    path('task/',TaskListCreateAPIView.as_view(), name='Task-list-create'),
    path('task/<int:pk>/', TaskRetrieveUpdateAPIView.as_view(), name='Task-list-create'),
    
    # Create Attendance URLs
    path('attendance/', AttendanceListCreateAPIView.as_view(), name='Attendance-List-Create'),
    path('attendance/<int:pk>/',  AttendanceRetrieveUpdateDestroyAPIView.as_view(), name='Attendance-Details'),
    
    # Create Account URLs
    path('account/', AccountListCreateAPIView.as_view(), name='Account-List-Create'),
    path('account/<int:pk>/', AccountRetrieveUpdateDestroyAPIView.as_view(), name='Account-Details'),
    
    # Create Salary URLs
    path('salary/', SalaryListCreateAPIView.as_view(), name='Salary-List-Create'),
    path('salary/<int:pk>/',SalaryRetrieveUpdateDestroyAPIView.as_view(), name='Salary-Details')
   
]