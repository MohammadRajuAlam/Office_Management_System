from rest_framework import serializers
import re # Regulare Expresion Modules use for validation
from office_managementapp.models import Department, Employee, EmployeeDetails, Project, Task, Attendance, Account, Salary

# Here create ModelSerializer of Department model
class DepartmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Department
        fields='__all__'
        read_only=['id','created_at','updated_at']
        
        # Here create a method for validate the Department fields
    # def validate(self, data):
    #     pass
        
        # Here This method is used to create a new instance/objects of the Department model.
    def create(self, validated_data):
        return Department.objects.create(**validated_data)
        
        # 1 way is Best way and handle larges fields in real time project
        # Here This method is used to update an existing instance of Employee model.
    def update(self, instance, validated_data):
        
        non_updatable_fields = ['department_id']  # Exclude fields that should not be updated and By using the non_updatable_fields list and checking each field before updating, we make sure that these fields retain their original values, even if they are present in the validated data.
        for key, value in validated_data.items():
            if key not in non_updatable_fields:
                setattr(instance, key, value) # Here setattr predefine function which is used to set the attribute values dynamically.
                
        instance.save()
        return instance
    
    """
        # OR 2nd ways to update Department instance/objects
    def update(self, instance, validated_data):
        instance.department_name=validated_data.get('validated_data', instance.department_name)
        instance.phone=validated_data.get('phone', instance.phone)
        instance.email=validated_data.get('email', instance.email)
        instance.is_active=validated_data.get('is_active', instance.is_active)
        instance.description=validated_data.get('description', instance.description)
        instance.save()
        return instance
    """

# Here Create ModelSerializer of Employee model          
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'
        read_only=('id','created_at','updated_at')
        
    # Here create a method for validate all fields of Employee model
    # def validate(self, validated_data):
    #     pass
    
    # Here create a method for insert/post/create a new records/instance in Employee instance
    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
    
    # Here create a method for update Employee instance
    def update(self, instance, validated_data):
        
        non_update_fields=['employee_id']
        for key, value in validated_data.items():
            if key not in non_update_fields:
                setattr(instance, key, value)
            
        instance.save()
        return instance

# Here create ModelSerializer of EmployeeDetails Model
class EmployeeDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=EmployeeDetails
        fields='__all__'
        read_only=['id','created_at','updated_at']
        
    # def validate(self, validated_data):
    #     pass
        
    def create(self, validated_data):
        return EmployeeDetails.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        
        for key, value in validated_data.items():
                setattr(instance, key, value) 
        
        instance.save
        return instance

# Here create a ModelSrializer of Project model  
class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Project
        fields='__all__'
        read_only=['id','created_at', 'updated_at']
        
    # def validate(self, validated_data):
    #     pass
    
    def create(self, validated_data):
        return Project.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        
        non_update_fields=['project_id']
        for key, value in validated_data.items():
            if key not in non_update_fields:
                setattr(instance, key, value)
                
        instance.save()
        return instance

# Here create ModelSerializer class for Task model    
class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Task
        fields='__all__'
        read_only=['id','created_at','updated_at']
        
    def validate(self, validated_data):
        
        pass
    
    def create(self, validated_data):
        return Task.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        
        non_update_field=['task_id']
        for key, value in validated_data.items():
            if key not in non_update_field:
                setattr[instance, key, value]
                
        instance.save()
        return instance
    
# Here create ModelSerialiser for Attendance Model
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields='__all__'
        read_only=('id',)
        
    def validate(self, validated_data):
        pass
    
    def create(self, validated_data):
        return Attendance.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        
        none_update_fields=['date']
        for key, value in validated_data.items():
            if key not in none_update_fields:
                setattr(instance, key, value) 
        instance.save()
        return instance
    
# Here create ModelSerializer for Account Model

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields='__all__'
        read_only=('id','created_at','updated_at')
        
    def validate(self, validated_data):
        pass
    
    def create(self, validated_data):
        return Account.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        
        non_update_fields=['account_number']
        for key, value in validated_data.items():
            if key not in non_update_fields:
                setattr(instance, key, value)
                
        instance.save()
        return instance
    
# Here create a ModelSerialiser for Salary model

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model=Salary
        fields='__all__'
        read_only=('id','date')
        
    def validate(self, validated_data):
        pass
    
    def create(self, validated_data):
        return Salary.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        
        for key, value in validated_data.items():
            setattr(instance, key, value)
            