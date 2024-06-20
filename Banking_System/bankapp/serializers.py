from rest_framework import serializers
#import re # Here importing Regular expression module for validation
from bankapp.models import Bank, Branch, Account, AccountHolder, Transaction

"""
# Here I am using Serializer Class from Rest_Framework

class BankSerializer(serializers.Serializer):
    bank_name = serializers.CharField(max_length=100)
    bank_id=serializers.CharField(max_length=10)
    '''
    Bank_Types=(('Goverment','Goverment'),
               ('Semi Goverment','Semi Goverment'),
               ('Private','Private'),
               ('Semi Private','Semi Private')) # Here having 2 elements in tuple. First element represents value and stored in database and send element represents human-readable name displayed in forms or admin panels.
    bank_type=serializers.CharField(max_length=30, choices=Bank_Types) '''
    # OR We can write only one line
    bank_type=serializers.ChoiceField(choices=Bank.Bank_Types)
    address=serializers.CharField(max_length=255)
    city=serializers.CharField(max_length=100)
    pincode=serializers.IntegerField()
    state=serializers.CharField(max_length=50)
    country=serializers.CharField(max_length=50, default='India')
    phone=serializers.IntegerField()
    email=serializers.EmailField(max_length=40)
    is_active=serializers.BooleanField(default=True)
    about=serializers.CharField(required=False,allow_null=False, allow_blank=False)
    created_at=serializers.DateField(read_only=True)
    updated_at=serializers.DateTimeField(read_only=True)
"""
# OR Using ModelSerializer Class from Rest_framework

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bank
        fields='__all__' # Here __all__ define all fields
        read_only=('id','created_at','updated_at')
        # fields=['bank_name','bank_id','address'] # here Defines particular or specific field
        #exclude=['id',] # Here serialize all fields except id
    
    # Here i am creating a validation function for validate all fields of Bank Class Model
    
    def validate(self, data):
        
        errors={}
        
        # validate bank_name
        bank_name=data.get('bank_name').strip()
        if not all(word.isalpha() for word in bank_name.split()):
            errors['bank_name']="Name should be only char"
        
        # validate bank_id    
        bank_id=data.get('bank_id').strip()
        if not bank_id.isalnum() or len(bank_id) !=10 or bank_id.isalpha() or bank_id.isdigit():
            errors['bank_id']='id should be isalnum without space and min 10 char'
        
        # validate city    
        city=data.get('city').strip()
        if not all(word.isalpha() for word in city.split()):
            errors['city']='city name should be only char'
        
        # validate pincode
        pincode=data.get('pincode')
        if len(str(pincode)) !=6:
            errors['pincode']='pincode exactly 6 digit'
        
        # validate state    
        state=data.get('state').strip()
        if not all(word.isalpha() for word in state.split()):
            errors['state']='name should be only characters'
        
        # validate country  
        country=data.get('country').strip()
        if not all(word.isalpha() for word in country.split()):
            errors['country']='Country name should be only character'
        
        # validate phone
        phone=data.get('phone')
        if len(str(phone)) !=10:
            errors['phone']="phone number exactly 10 digit"
            
        # Validate email
        email = data.get('email').strip()
        if not email.endswith("@gmail.com"):
            errors["email"] = "Email should end with @gmail.com."
        
        if errors:
             raise serializers.ValidationError(errors)
        return data
    
    # Here I am defining a function for create/insert/Post the records (rows, objects) & return a new Bank instancein Bank class models
    def create(self, validated_data):
        """
        creat/insert new Bank instance (object)
        """
        return Bank.objects.create(**validated_data)
    
    # Here defining a function for Update and return an existing Bank instance (objects)
    def update(self, instance, validated_data): # Here in instance having existing object and new/update data comes in validated_data  
        """
        update an existing Bank instance
        """
        instance.bank_name=validated_data.get('bank_name', instance.bank_name)  # Here updating every fields manually
        instance.bank_type=validated_data.get('bank_type', instance.bank_type)
        instance.address=validated_data.get('address', instance.address)
        instance.pincode=validated_data.get('pincode', instance.pincode)
        instance.state=validated_data.get('state', instance.state)
        instance.country=validated_data.get('country', instance.country)
        instance.phone=validated_data.get('phone', instance.phone)
        instance.email=validated_data.get('email', instance.email)
        instance.is_active=validated_data.get('is_active', instance.is_active)
        instance.about=validated_data.get('about', instance.about)
        instance.save()
        return instance

    # OR Here write in short code for update the objects (records) using for loop
    """
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    """ 
"""        
class BranchSerializer(serializers.Serializer):
    branch_name=serializers.CharField(max_length=100)
    branch_id=serializers.CharField(max_length=10)
    address=serializers.CharField(max_length=255)
    city=serializers.CharField(max_length=50)
    pincode=serializers.IntegerField()
    country=serializers.CharField(max_length=50, default='India')
    phone=serializers.IntegerField()
    email=serializers.EmailField(max_length=40)
    is_active=serializers.BooleanField(default=True)
    bank=serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())  # Here Relastionship with Bank
    created_at=serializers.DateField(auto_now_add=True)
    updated_at=serializers.DateTimeField(auto_now_add=True)
"""
# OR

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Branch
        fields='__all__'
        read_only=['id','created_at','update_at']
         
    def validate(self, data):
        errors={}
        
        # validate branch name
        branch_name=data.get('branch_name').strip()
        if not all(word.isalpha() for word in branch_name.split()):
            errors['branch_name']='Name should be character'
            
        if errors:
            raise serializers.ValidationError(errors)
        
        return data
    
    def create(self, validated_data):
        """
        create a new Branch instance
        """
        return Branch.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.branch_name=validated_data.get('branch_name', instance.branch_name)
        instance.address=validated_data.get('address', instance.address)
        instance.pincode=validated_data.get('pincode', instance.pincode)
        instance.country=validated_data.get('country', instance.country)
        instance.phone=validated_data.get('phone', instance.phone)
        instance.email=validated_data.get('email', instance.email)
        instance.is_active=validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance
    
class AccountSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields='__all__'
        read_only=['id','create_at','updated_at']
    
    # def validate_branch(self, data):
    #     pass
    
    def create(self, validated_data):
        """
        insert a new record in Account Model
        """
        return Account.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.balance=validated_data.get('balance', instance.balance)
        instance.account_type=validated_data.get('account_type', instance.account_type)
        instance.is_active=validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance

class AccountHolderSerializer(serializers.ModelSerializer):
    class Meta:
        model=AccountHolder
        fields='__all__'
        read_only=('id','created_at','updated_at')
        
    # def validate(self, data):
         #pass
    
    def create(self, validated_data):
        """
        insert a new record in AccounHolder model
        """
        return AccountHolder.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.holder_name=validated_data.get('holder_name', instance.holder_name)
        instance.date_of_birth=validated_data.get('date_of_birth', instance.date_of_birth) # DOB do't use future date for DOB
        instance.father_name=validated_data.get('father_name', instance.father_name)
        instance.mother_name=validated_data.get('mother_name', instance.mother_name)
        instance.qualification=validated_data.get('qualification', instance.qualification)
        instance.address=validated_data.get('address', instance.address)
        instance.city=validated_data.get('city', instance.city)
        instance.pincode=validated_data.get('pincode', instance.pincode)
        instance.state=validated_data.get('state', instance.state)
        instance.country=validated_data.get('country', instance.country)
        instance.phone=validated_data.get('phone', instance.phone)
        instance.email=validated_data.get('email', instance.email)
        instance.is_alive=validated_data.get('is_alive', instance.is_alive)
        instance.save()
        return instance
    
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields='__all__'
        read_only=['id','transaction_date']
        
    # def validate(self, data):
    #     pass
    
    def create(self, validated_data):
        """
        insert a new record in Transaction models
        """
        return Transaction.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        update in existing Transaction models
        """
        instance.transaction_type=validated_data.get('transaction_type', instance.transaction_type)
        instance.amount=validated_data.get('amount', instance.amount)
        instance.save()
        return instance