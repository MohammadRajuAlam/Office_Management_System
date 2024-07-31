from django.db import models

# Creating Soft Delete models
class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()
    all_objects = models.Manager()  # Includes soft-deleted records

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()
    class Meta:
        abstract = True 
         
# Here I am creating Office Management System Models
class Department(SoftDeleteModel):
    department_name = models.CharField(
        max_length=50,
        unique=True,
        error_messages={
            'unique': 'Given name already exists.'
        }
    )
    department_id = models.CharField(
        max_length=10,
        unique=True,
        error_messages={
            'unique': 'Given ID is already used.'
        }
    )
    phone = models.PositiveBigIntegerField(
        unique=True,
        error_messages={
            'unique': 'Given number is already used.'
        }
    )
    email = models.EmailField(
        max_length=30,
        unique=True,
        error_messages={
            'unique': 'Given Email ID is already used.'
        }
    )
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.department_name}'

class Employee(SoftDeleteModel):
    first_name = models.CharField(max_length=10)
    middle_name = models.CharField(max_length=10, null=True, blank=True)
    last_name = models.CharField(max_length=10)
    employee_id = models.CharField(
        max_length=10,
        unique=True,
        error_messages={
            'unique': 'Given ID is already used.'
        }
    )
    emp_salary = models.CharField(max_length=50, null=True, blank=True)
    designation = models.CharField(max_length=50)
    total_experience = models.FloatField(default=0)
    date_of_join = models.DateField()
    highest_degree = models.CharField(max_length=50)
    phone = models.PositiveBigIntegerField(
        unique=True,
        error_messages={
            'unique': 'Given number is already used.'
        }
    )
    email = models.EmailField(
        max_length=30,
        unique=True,
        error_messages={
            'unique': 'Given email ID is already used.'
        }
    )
    is_working_here = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='department')
    
    def __str__(self):
        
        return f"{self.first_name+' '+self.last_name}"
        #return f"{self.id} {self.first_name}"

class EmployeeDetails(SoftDeleteModel):
    employee_aadhaar = models.PositiveBigIntegerField(
        unique=True,
        error_messages={
            'unique': 'Given Aadhaar number already exists.'
        }
    )
    father_name = models.CharField(max_length=20)
    house_phone_number = models.PositiveBigIntegerField(
        null=True,
        blank=True,
        unique=True,
        error_messages={
            'unique': 'Given phone number already exists.'
        }
    )
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()
    country = models.CharField(max_length=50, default='India')
    date_of_birth = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='employeedetails')
    
    def __str__(self):
        return f'{self.employee_aadhaar}'

class Project(SoftDeleteModel):
    project_name = models.CharField(max_length=100)
    project_id = models.CharField(
        max_length=10,
        unique=True,
        error_messages={
            'unique': 'Given project ID already exists.'
        }
    )
    technologies_used = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='project')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='project')
    
    def __str__(self):
        return f'{self.project_name}'

class Task(SoftDeleteModel):
    task_name = models.CharField(max_length=100)
    task_id = models.CharField(
        max_length=10,
        unique=True,
        error_messages={
            'unique': 'Task ID already exists.'
        }
    )
    project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='task')
    TASK_STATUS = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    ]
    task_status = models.CharField(max_length=20, choices=TASK_STATUS)
    start_date = models.DateField()
    end_date = models.DateField()
    task_description = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='task')
    
    def __str__(self):
        return f'{self.task_name}'

class Attendance(SoftDeleteModel):
    date = models.DateField()
    ATTENDANCE_STATUS = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Leave', 'Leave')
    ]
    attendance_status = models.CharField(max_length=20, choices=ATTENDANCE_STATUS)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='attendance')
    
    def __str__(self):
        return f'{self.date} {self.employee}'

class Account(SoftDeleteModel):
    bank_name = models.CharField(max_length=50)
    account_number = models.PositiveBigIntegerField(
        unique=True,
        error_messages={
            'unique': 'Given account number is already used.'
        }
    )
    ACCOUNT_TYPES = [
        ('Current', 'Current'),
        ('Saving', 'Saving'),
        ('Salary','Salary'),
        ('Joint', 'Joint')
    ]
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    balance = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    employee = models.OneToOneField(Employee, on_delete=models.PROTECT, related_name='account')
    
    def __str__(self):
        return f'{self.account_number} {self.bank_name}'

class Salary(SoftDeleteModel):
    amount = models.FloatField(default=0)
    account_number = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='salary')
    date = models.DateField(auto_now_add=True)
    remark = models.CharField(max_length=100, null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='salary')

    def __str__(self):
        return f'{self.amount}'

    def deposit(self):
        self.account_number.balance += self.amount
        self.account_number.save()

    def save(self, *args, **kwargs):
        if not self.pk:  # If the object is being created, not updated
            self.deposit()
        super(Salary, self).save(*args, **kwargs)