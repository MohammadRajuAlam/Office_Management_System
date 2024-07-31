from django.contrib import admin
from employeeapp.models import Department, Employee, EmployeeDetails, Project, Task, Attendance, Account, Salary

# Register your models here.
# admin.site.register(Department)
# OR
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=['id','department_name','department_id','phone','email','is_active','description','created_at','updated_at']
    
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','first_name','middle_name','last_name','designation','emp_salary','department','total_experience','date_of_join','highest_degree','phone','email','is_working_here','created_at','updated_at']
    
@admin.register(EmployeeDetails)
class EmployeedetailsAdmin(admin.ModelAdmin):
    list_display=['id','employee_aadhaar','father_name','house_phone_number','address','city','state','pincode','country','date_of_birth','created_at','updated_at']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=['id','project_name','project_id','technologies_used','start_date','end_date','description','employee','department','created_at','updated_at']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=['id','task_name','task_id','project','task_status','start_date','end_date','assigned_to','task_description','created_at','updated_at']
    
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display=['id','date','attendance_status','employee','created_at','updated_at']
    
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display=['id','bank_name','account_number','account_type','balance','employee','is_active','created_at','updated_at']
    
@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display=['id','amount','account_number','date','employee','remark']