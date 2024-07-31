from rest_framework import serializers
from employeeapp.models import Department, Employee, EmployeeDetails, Project, Task, Attendance, Account, Salary
from datetime import date, timedelta

# Here create Department Serializer with inherit Model Serializer
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields='__all__' # Here Access and display all models class fields
        read_only_fields=('id','created_at','updated_at') # These fields are only readiable fields 
    
    # Here create a method for validation of Departments fields  
    def validate(self, data):
        
        errors = {}
        
        # department name validate
        department_name = data.get('department_name',None)
        if department_name is not None:
            department_name = department_name.strip()
            if not all(word.isalpha() for word in department_name.split()):
                errors['department_name'] = "Name should be characters"
        
        # department id validate Here you don't want to update or change ID after created ID write these Logic
        department_id = data.get('department_id', None)
        if self.instance: # Here Checks if the serializer is working with an existing instance of Department.
            # If instance already exists, ensure Department ID cannot be updated
            if 'department_id' in data and data['department_id'] !=self.instance.department_id:
                errors['department_id']="Department ID can't be updated once set."
                
        elif department_id is not None:
            department_id=department_id.strip()
            if len(department_id) != 10 or not department_id.isalnum() or department_id.isalpha() or department_id.isdigit():
                errors['department_id']="ID must be contains char with number 10 words."
        
        # phone number validate       
        phone = data.get('phone',None)
        if phone is not None:
            if len(str(phone)) !=10:
                errors['phone']='Number should be 10 digit.'
        
        # email id validate
        email = data.get('email',None)
        if email is not None:
            email = email.strip()
            if not email.endswith('@gmail.com'):
                errors['email']='Email must be end with @gmail.com'
        
        # description validate
        description = data.get('description', None)
        if description is not None:
            description = description.strip()
            if description.isdigit():
                errors['description']="Can't use only digit." 
        if errors:
            raise serializers.ValidationError(errors)
        return data
    
class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()
    class Meta:
        model=Employee
        fields='__all__'
        read_only_fields=('id','created_at','updated_at')
    
    # Here create a method for validation of Employee fields  
    def validate(self, data):
        
        errors={}
        
        # first name validate
        first_name = data.get('first_name', None)
        if first_name is not None:
            first_name = first_name.strip()
            if not all(word.isalpha() for word in first_name.split()):
                errors['first_name']='Name should be character.'
        
        # middle name validate
        middle_name = data.get('middle_name', None)
        if middle_name is not None:
            middle_name = middle_name.strip()
            if not all(word.isalpha() for word in middle_name.split()):
                errors['middle_name']='Name should be character.'
        
        # last name validate
        last_name = data.get('last_name', None)
        if last_name is not None:
            last_name = last_name.strip()
            if not all(word.isalpha() for word in last_name.split()):
                errors['last_name']='Name should be character.'
        
        # Employee Id validate
        employee_id = data.get('employee_id',None)
                
        if employee_id is not None:
            employee_id = employee_id.strip()
            if len(employee_id) !=10 or not employee_id.isalnum() or employee_id.isalpha() or employee_id.isdigit():
                errors['employee_id']="ID must contains character and number with 10 words."
                
        elif self.instance:
            if 'employee_id' in data and data['employee_id'] !=self.instance.employee_id:
                errors['employee_id'] = "Employee ID can't update."
                
        designation = data.get('designation', None)
        if designation is not None:
            designation = designation.strip()
            if not all(word.isalpha() for word in designation.split()):
                errors['designation']='Given Designation should be characters.'
           
        total_experience = data.get('total_experience', None)
        if total_experience is not None and total_experience<0 :
            errors['total_experience']="Experience can't be negativ."
        elif total_experience>30:
            errors['total_experience']="Experience can't be more than 30 years."
        
        date_of_join = data.get('date_of_join',None)
        if date_of_join is not None:
            if date_of_join > date.today():
                errors['date_of_join']="Can't select Future Date."
                
        highest_degree = data.get('highest_degree', None)
        if highest_degree is not None:
            highest_degree = highest_degree.strip() 
            if highest_degree.isdigit():
                errors['highest_degree']="Degree can't take only digit"
                
        phone = data.get('phone', None)
        if phone is not None and len(str(phone)) !=10:
                errors['phone']='Phone number should be 10 digit.'
                
        email = data.get('email',None) 
        if email is not None:
            email = email.strip()
            if not email.endswith('@gmail.com'):
                errors['email']='email ID must be end with @gmail.com'
                
        if errors:
            raise serializers.ValidationError(errors)
        return data
    
class EmployeeDetailsSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField()
    class Meta:
        model=EmployeeDetails
        fields='__all__'
        read_only_fields=('id','created_at','updated_at')
        
    # Here create a method for validation of EmployeeDetails fields  
    def validate(self, data):
        
        errors = {}
    
        employee_aadhaar = data.get('employee_aadhaar',None)
        if self.instance: # Here Checks if the serializer is working with an existing instance of EmployeeDetails
            
            # If instance already exists, ensure Aadhaar number cannot be updated
            if 'employee_aadhaar' in data and data['employee_aadhaar'] != self.instance.employee_aadhaar:
                errors['employee_aadhaar'] = "Aadhaar number can't be updated once set."
                
        elif employee_aadhaar is not None and len(str(employee_aadhaar)) !=12:
                errors['employee_aadhaar']='Aadhaar Number should be 12 digit.'
        
        father_name = data.get('father_name', None)
        if father_name is not None:
            father_name = father_name.strip()
            if not all(word.isalpha() for word in father_name.split()):
                errors['father_name']='Name should be characters.'
                
        phone = data.get('house_phone_number',None)
        if phone is not None and len(str(phone)) !=10:
                errors['house_phone_number']='phone number should be 10 digit.'
                
        address =data.get('address', None)
        if address is not None:
            address = address.strip()
            if address.isdigit():
                errors['address']="Address can't take only digit"
        
        city = data.get('city',None)
        if city is not None:
            city = city.strip()
            if not all(word.isalpha() for word in city.split()):
                errors['city']='city name should be characters.'
                
        state = data.get('state',None)
        if state is not None:
            state = state.strip()
            if not all(word.isalpha() for word in state.split()):
                errors['state']='state Name should be Characters.'
                
        pincode = data.get('pincode',None)
        if pincode is not None and len(str(pincode)) !=6:
                errors['pincode']='PinCode must 6 digit.'

        country = data.get('country',None)
        if country is not None:
            country = country.strip()
            if not all(word.isalpha() for word in country.split()):
                errors['country']='Country name should be characters.'
            
        date_of_birth = data.get('date_of_birth', None)
        if date_of_birth is not None and date_of_birth > date.today():
            errors['date_of_birth']="Can't take future date for date_of_birth."
        elif date_of_birth> date.today() - timedelta(days=18*365):
            errors['date_of_birth']='Age must be above 18 years.'
        
        if errors:
            raise serializers.ValidationError(errors)
        return data
        
class ProjectSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField()
    department = serializers.StringRelatedField()
    class Meta:
        model=Project
        fields='__all__'
        read_only_fields=('id','created_at','updated_at')
        
    # Here create a method for validation of Project fields  
    def validate(self, data):
        
        errors = {}
        
        project_name = data.get('project_name', None)
        if project_name is not None:
            project_name = project_name.strip()
            if project_name.isdigit():   # Here Project Name can be char with number.
                errors['project_name']="Project Name can't take only numbers."
                
        project_id = data.get('project_id', None)
        if project_id is not None:
            project_id = project_id.strip()
            if len(project_id) !=10 or not project_id.isalnum() or project_id.isalpha() or project_id.isdigit():
                errors['project_id']='ID must contains char with numbers and 10 words.'
                
        elif self.instance:
            if 'project_id' in data and data['project_id'] != self.instance.project_id:
                errors['project_id'] = "Project ID can't be updated."
                
        technologies_used = data.get('technologies_used',None)
        if technologies_used is not None:
            technologies_used = technologies_used.strip()
            if technologies_used.isdigit():
                errors['technologies_used']="technologies can't Take only numbers."
        
        description = data.get('description', None)
        if description is not None:
            description = description.strip()
            if description.isdigit():
                errors['description']="Description can't take only digit."        
        
        start_date = data.get('start_date', None)
        end_date = data.get('end_date', None)
        
        # Ensure that start_date is not after end_date
        if start_date and end_date:
            if start_date > end_date:
                errors['start_date'] = 'Start date cannot be after the end date.'
                errors['end_date'] = 'End date cannot be before the start date.'
                
        if errors:
            raise serializers.ValidationError(errors)
        return data
    
class TaskSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    assigned_to = serializers.StringRelatedField()
    class Meta:
        model=Task
        fields='__all__'
        read_only_fields=('id','created_at','updated_at')
        
    # Here create a method for validation of Task fields  
    def validate(self, data):
        errors = {}
        
        # task_name validate
        task_name = data.get('task_name', None)
        if task_name is not None:
            task_name = task_name.strip()
            if not all(word.isalpha() for word in task_name.split()):
                errors['task_name'] ='Name should be Characters.'
        task_id = data.get('task_id',None)
        if task_id is not None:
            task_id = task_id.strip()
            if len(task_id) !=10 or not task_id.isalnum or task_id.isalpha() or task_id.isdigit():
                errors['task_id']='Task ID must be 10 characters with numbers'
            
        elif self.instance: # task_id can't changed/updat
            if 'task_id' in data and data['task_id'] != self.instance.task_id:
                errors['task_id'] = "Task ID can't be updated."
            
        start_date = data.get('start_date', None)
        end_date = data.get('end_date', None)
        
        # Ensure that start_date is not after end_date
        if start_date and end_date:
            if start_date > end_date:
                errors['start_date'] = 'Start date cannot be after the end date.'
                errors['end_date'] = 'End date cannot be before the start date.' 
        
        task_description = data.get('task_description',None)
        if task_description is not None:
            task_description = task_description.strip()
            if task_description.isdigit():
                errors['task_description']="Task description can't take only number"    
        if errors:
            raise serializers.ValidationError(errors)
        return data

class AttendanceSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField()
    class Meta:
        model=Attendance
        fields='__all__'
        read_only_fields=('id','created_at','updated_at')
        
    # Here create a method for validation of Attendance fields  
    def validate(self, data):
        
        errors = {}
        
        dates = data.get('date', None)
        if dates is not None:
            if dates>date.today():
                errors['date']="Attendance Date can't take future date."            
        if errors:
            raise serializers.ValidationError(errors)
        return data
        
class AccountSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField()
    class Meta:
        model=Account
        fields='__all__'
        read_only_fields=('id','created_at','updated_at')
        
    # Here create a method for validation of Account fields  
    def validate(self, data):
        
        errors = {}
        bank_name = data.get('bank_name', None)
        if bank_name is not None:
            bank_name = bank_name.strip()
            if not all(word.isalpha() for word in bank_name.split()):
                errors ['bank_name']='Bank name should be character.'
        
        account_number = data.get('account_number', None)
        if account_number is not None and len(str(account_number)) !=14:
                errors['account_number']='Account number should be 14 digit.'
        elif self.instance:
            if 'account_number' in data and data['account_number'] != self.instance.account_number:
                errors['account_number'] = "Account number can't be updated."
                
        elif self.instance:
            if 'account_number' in data and data['account_number'] != self.instance.account_number:
                errors['account_number'] = "Account number can't be updated."
        if errors:
            raise serializers.ValidationError(errors)
        return data
    
class SalarySerializer(serializers.ModelSerializer):
    account_number = serializers.StringRelatedField()
    employee = serializers.StringRelatedField()
    class Meta:
        model=Salary
        fields='__all__'
        read_only_fields=('id','created_at','updated_at')
        
    # Here create a method for validation of Salary fields  
    def validate(self, data):
        
        errors = {}
        
        amount = data.get('amount', None) 
        if amount is not None and amount<0:
                errors['amount']="Amount can't less than 0."
             
        remark = data.get('remark',None) 
        if remark is not None:
            remark = remark.strip()
            if remark.isdigit():
                errors['remark'] = "Remark can't take only digit."
        if errors:
            raise serializers.ValidationError(errors)
        return data