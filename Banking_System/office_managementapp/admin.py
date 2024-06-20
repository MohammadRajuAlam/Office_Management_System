from django.contrib import admin
from office_managementapp.models import Department, Employee, EmployeeDetails, Project, Task, Attendance, Account, Salary

"""
# 1st way to Register models in admin File like -
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Employee)
admin.site.register(EmployeeDetails)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Attendance)
admin.site.register(Account)
admin.site.register(Salary)
"""

# OR 2nd way is Best to Register models with fields name in admin File like -

# Register Department model with customization
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'department_name', 'department_id', 'phone', 'email', 'is_active', 'description', 'created_at', 'updated_at']

# Register Employee model with customization
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'middle_name', 'last_name', 'employee_id', 'phone', 'email', 'designation', 'date_of_join', 'highest_degree', 'total_experience', 'is_working_here', 'created_at', 'updated_at']

# Register EmployeeDetails model with customization
@admin.register(EmployeeDetails)
class EmployeeDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'address', 'city', 'pincode', 'state', 'country', 'father_name', 'created_at', 'updated_at']

# Register Project model with customization
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'project_name', 'project_id', 'tech_used', 'description', 'start_date', 'end_date', 'departement', 'employee','created_at','updated_at']

# Register Task model with customization
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'task_name', 'task_id', 'task_status', 'start_date', 'end_date', 'project', 'assigned_to', 'created_at', 'updated_at']

# Register Attendance model with customization
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'attendance_status', 'date']

# Register Account model with customization
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'bank_name', 'account_number', 'balance', 'employee', 'is_active', 'created_at', 'updated_at']

# Register Salary model with customization
@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ['id', 'account', 'amount', 'employee', 'remark', 'date']
