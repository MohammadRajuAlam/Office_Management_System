from django.db import models
from django.utils import timezone
import random

###### Here I am creating models for office Management with Soft Delete Concepts

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = SoftDeleteManager()
    all_objects = models.Manager()  # To access both deleted and non-deleted objects

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True

# Here create Department Model    
class Department(SoftDeleteModel):    # Here inherit SoftrDeleteModel
    department_name=models.CharField(
        max_length=50,
        unique=True,
        error_messages={
            'unique':'Given department already Existing'
        }
    )
    department_id=models.CharField(
        max_length=10,
        unique=True,
        error_messages={
            'unique':'Given id already Existing'
            }
        )
    phone=models.PositiveBigIntegerField(
        unique=True,
        error_messages={
            'error':'Given number is already used.'
            }
        )
    email=models.EmailField(
        null=True,
        blank=True,
        unique=True,
        error_messages={
            'unique':'Given Email Id is already used.'
        }
    )
    is_active=models.BooleanField(default=True)
    description=models.TextField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.department_name}'
    
    class Meta:
        ordering = ['department_name']

# Employee Model
class Employee(SoftDeleteModel):
    department=models.ForeignKey(
        Department,
        on_delete=models.CASCADE)
    first_name=models.CharField(max_length=15)
    middle_name=models.CharField(
        max_length=15,
        null=True,
        blank=True
        )
    last_name=models.CharField(max_length=15)
    employee_id=models.CharField(
        max_length=10,
        null=True,
        unique=True,
        error_messages={
            'unique':'Given Employee Id is already exist.'
        }
    )
    #upload_your_photo=models.ImageField(null=True, blank=True) # ?????????
    date_of_birth=models.DateField()
    phone=models.PositiveBigIntegerField(
        unique=True,
        error_messages={
            'error':'Given number is already used.'
        }
    )
    email=models.EmailField(
        unique=True,
        error_messages={
            'unique':'Given Email Id is already used.'
        }
    )
    designation=models.CharField(max_length=50)
    date_of_join=models.DateField()
    highest_degree=models.CharField(max_length=50)
    total_experience=models.CharField(
        max_length=50,
        default="0")
    is_working_here=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering=['first_name']

# Employee Details Model   
class EmployeeDetails(SoftDeleteModel):
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    # aadhaar_no=models.PositiveBigIntegerField(
    #     unique=True,
    #     error_messages={
    #         'unique':'given Addhaar number is already Exist.'
    #         }
    #     )
    #upload_aadhaar_pdf=models.FileField(null=True, blank=True)  # ??????????
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=50)
    pincode=models.PositiveIntegerField()
    state=models.CharField(max_length=50)
    country=models.CharField(
        max_length=50,
        default="India")
    father_name=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.employee}'

# Project Model   
class Project(SoftDeleteModel):
    project_name=models.CharField(max_length=300)
    project_id=models.CharField(
        max_length=10,
        unique=True,
        error_messages={
            'unique':'Given Project Id is existing'
            }
        )
    tech_used=models.CharField(max_length=20)
    description=models.TextField()
    start_date=models.DateField()
    end_date=models.DateField()
    departement=models.ForeignKey(Department, on_delete=models.CASCADE)
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.project_name}'
    
    class Meta:
        ordering=['project_name']

# Task Model
class Task(SoftDeleteModel):
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    task_name=models.CharField(
        max_length=300,
        default="")
    task_id=models.CharField(
        max_length=5,
        unique=True,
        error_messages={
            'unique':'Task Id is Existing'
            }
        )
    TASK_STATUS=[
        ('Pending','Pending'),
        ('In Progress', 'In Progress'),
        ('Completed','Complated')
    ]
    task_status=models.CharField(
        max_length=25,
        choices=TASK_STATUS
    )
    start_date=models.DateField()
    end_date=models.DateField()
    task_description=models.TextField(null=True, blank=True)
    assigned_to=models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.task_name} {self.project}'
    
    class Meta:
        ordering=['task_name']
        
#  Attendence Model
class Attendance(SoftDeleteModel):
    ATTENDANCE_STATUS=[
        ('Present','Present'),
        ('Absent','Absent'),
        ('Leave','Leave')
    ]
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    attendance_status=models.CharField(max_length=25, choices=ATTENDANCE_STATUS)
    date=models.DateField()

# Account Model 
class Account(SoftDeleteModel):
    bank_name=models.CharField(max_length=50)
    account_number=models.PositiveBigIntegerField(
        unique=True,
        error_messages={
            'unique':'Given Account number is already Exist.'
        }
    )
    balance=models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
        )
    employee=models.OneToOneField(Employee, on_delete=models.CASCADE)
    ACCOUNT_TYPE=[
        ('Salary Acc','Salary Acc'),
        ('Saving Acc','Saving Acc'),
        ('Joint Acc','Joint Acc')
    ]
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.account_number} {self.balance}'
    
    class Meta:
        ordering=['account_number']

# Salary Model    
class Salary(SoftDeleteModel):
    account=models.ForeignKey(Account, on_delete=models.CASCADE)
    amount=models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
        )
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)

    remark=models.TextField(null=True, blank=True)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.amount} {self.account}'
    
    class Meta:
        ordering=['amount']