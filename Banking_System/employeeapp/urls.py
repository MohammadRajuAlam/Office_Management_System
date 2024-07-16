from django.contrib import admin
from django.urls import path
from employeeapp.views import (
    DepartmentListCreateAPIView,
    DepartmentRetrieveUpdateDestroyAPIView,
    EmployeeListCreateAPI,
    EmployeeRetrieveUpdateDestroyAPIView,
    DepartmentEmployeeAPIVie,
    EmployeeDetailsListCreateAPIView,
    EmployeeDetailsRetrieveUpdateDestroyAPIView,
    EmployeeEmployeeDetailsAPIView,
    ProjectListCreateAPIView,
    ProjectRetrieveUpdateAPIView,
    EmployeeProjectAPIView,
    TaskListCreateAPIView,
    TaskRetrieveUpdateAPIView,
    EmployeeTaskAPIView,
    AttendanceListCreateAPIView,
    AttendanceRetrieveUpdateDestroyAPIView,
    EmployeeAttendanceAPIView,
    AccountListCreateAPIView,
    AccountRetrieveUpdateDestroyAPIView,
    SalaryListCreateAPIView,
    SalaryRetrieveUpdateDestroyAPIView,
    )

urlpatterns = [
    # Her Created Department URLs
    path('departments/', DepartmentListCreateAPIView.as_view(), name='All-Department-list'),
    path('departments/<int:pk>/', DepartmentRetrieveUpdateDestroyAPIView.as_view(), name='Specific-Department-list'),
    
    # Here Created Employee URLs
    path('employees/', EmployeeListCreateAPI.as_view(), name='All-Employee-list'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='Specific-Employee-details'),
    # Custom URL to get all/Single employees of a specific department like department/1/employees  /1 # Here access all employees of department/1
    path('departments/<int:pk>/employees/', DepartmentEmployeeAPIVie.as_view(), name='Specific-Department-All-Employees-list'),
    path('departments/<int:pk>/employees/<int:empl_pk>/', DepartmentEmployeeAPIVie.as_view(), name='Specific-Department-Specific-Employees'),
    
    # Here Created Employee Details URLs
    path('employeeDetails/', EmployeeDetailsListCreateAPIView.as_view(), name='All-EmployeeDetails-list'),
    path('employeeDetails/<int:pk>/', EmployeeDetailsRetrieveUpdateDestroyAPIView.as_view(), name='Specific-EmployeeDetails-list'),
    # Custome URLs to get single/All EmployeeDetails of a specific Employee
    path('employees/<int:pk>/employeeDetails/', EmployeeEmployeeDetailsAPIView.as_view(), name='Specific-Employee-All-EmployeeDetails-list'),
    path('employees/<int:pk>/employeeDetails/<int:emp_detl_pk>/', EmployeeEmployeeDetailsAPIView.as_view(), name='Specifice-Employee-Specific-EmployeeDetails-list'),
    
    # Here Created project URLs
    path('project/', ProjectListCreateAPIView.as_view(), name='All-Project-list'),
    path('project/<int:pk>/',ProjectRetrieveUpdateAPIView.as_view(), name='Specific-Project-list'),
    # Custome URLs to get single/All Project of a specific Employee
    path('employees/<int:pk>/project/', EmployeeProjectAPIView.as_view(), name='Specific-Employee-All-Project-list'),
    path('employees/<int:pk>/project/<int:pro_pk>/', EmployeeProjectAPIView.as_view(), name='Specific-Employee-Specific-Project-list'),
    
    # Here Created Task URLs
    path('task/',TaskListCreateAPIView.as_view(), name='All-Task-list'),
    path('task/<int:pk>/', TaskRetrieveUpdateAPIView.as_view(), name='Specific-Task-list'),
    # Custome URLs to get single/All task of a specific Employee
    path('employees/<int:pk>/task/', EmployeeTaskAPIView.as_view(), name='Specific-Employee-All-Task-list'),
    path('employees/<int:pk>/task/<int:task_pk>/', EmployeeTaskAPIView.as_view(), name='Specific-Employee-Specific-Task-list'),
    
    # Here Created Attendance URLs
    path('attendance/', AttendanceListCreateAPIView.as_view(), name='All-Attendance-List'),
    path('attendance/<int:pk>/',  AttendanceRetrieveUpdateDestroyAPIView.as_view(), name='Specific-Attendance-list'),
    # Custome URLs to get single/All Attendance of a specific Employee
    path('employees/<int:pk>/attendance/', EmployeeAttendanceAPIView.as_view(), name='Specific-Emloyee-All-Attendance-list'),
    path('employees/<int:pk>/attendance/<int:attend_pk>/', EmployeeAttendanceAPIView.as_view(), name='Specific-Emloyee-Specific-Attendance-list'),
    
    # Here Created Account URLs
    path('account/', AccountListCreateAPIView.as_view(), name='All-Account-List'),
    path('account/<int:pk>/', AccountRetrieveUpdateDestroyAPIView.as_view(), name='Specific-Account-list'),
    # Custome URLs to get single/All Account of a specific Employee
    
    # Here Created Salary URLs
    path('salary/', SalaryListCreateAPIView.as_view(), name='All-Salary-List'),
    path('salary/<int:pk>/',SalaryRetrieveUpdateDestroyAPIView.as_view(), name='Specific-Salary-list'),
   
]