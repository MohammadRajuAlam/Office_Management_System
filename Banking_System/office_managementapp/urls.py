from django.contrib import admin
from django.urls import path, include
from office_managementapp.views import * # DepartmentAPI

urlpatterns = [
    path('department', DepartmentAPI.as_view(), name='DepartmentAPI'), # access/insert department
    path('department/<id>', DepartmentAPI.as_view(), name='DepartmentAPI'), # access specific department
    path('DepartmentDetail/<id>', DepartmentDetailAPI.as_view(), name='DepartmentDetailAPI'), # put/patch/delete department data
    
]