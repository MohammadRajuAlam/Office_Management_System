from rest_framework import serializers
from datetime import date, timedelta
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
        bank_name=data.get('bank_name',None) # Here taking None because when we do partial update that time don't fetch any error
        if bank_name is not None:
            bank_name=bank_name.strip()
            if not all(word.isalpha() for word in bank_name.split()):
                errors['bank_name']="Name should be only char"
        
        # validate bank_id    
        bank_id=data.get('bank_id', None)
        if bank_id is not None:
            bank_id=bank_id.strip()
            if not bank_id.isalnum() or len(bank_id) !=10 or bank_id.isalpha() or bank_id.isdigit():
                errors['bank_id']='id should be isalnum without space and min 10 char'
        
        # validate city    
        city=data.get('city',None)
        if city is not None:
            city=city.strip()
            if not all(word.isalpha() for word in city.split()):
                errors['city']='city name should be only char'
        
        # validate pincode
        pincode=data.get('pincode',None)
        if pincode is not None:
            if len(str(pincode)) !=6:
                errors['pincode']='pincode exactly 6 digit'
        
        # validate state    
        state=data.get('state',None)
        if state is not None:
            state=state.strip()
            if not all(word.isalpha() for word in state.split()):
                errors['state']='name should be only characters'
            
        # validate country  
        country=data.get('country',None)
        if country is not None:
            country=country.strip()
            if not all(word.isalpha() for word in country.split()):
                errors['country']='Country name should be only character'
        
        # validate phone
        phone=data.get('phone',None)
        if phone is not None:
            if len(str(phone)) !=10 or not str(phone).isdigit():
                errors['phone']="phone number exactly 10 digit"
            
        # Validate email
        email = data.get('email',None)
        if email is not None:
            email=email.strip()
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
        branch_name=data.get('branch_name',None)
        if branch_name is not None:
            branch_name=branch_name.strip()
            
            if not all(word.isalpha() for word in branch_name.split()):
                errors['branch_name']='Name should be character'
        
        # validate branch_id    
        branch_id=data.get('branch_id', None)
        if branch_id is not None:
            branch_id=branch_id.strip()
            if len(branch_id) !=10 or not all(word.isalnum() for word in branch_id) or branch_id.isalpha() or branch_id.isdigit():
                errors['branch_id']='branch_id must be contains char and number with 10 elements'
        
        # validate the Address  
        address=data.get('address', None)
        if address is not None:
            address=address.strip() 
            if address.isdigit():
                errors['address']="address can't only Digit"
        
        # validate pincode  
        pincode=data.get('pincode', None)
        if pincode is not None:
            if len(str(pincode)) !=6:
                errors['pincode']="pincode exactly 6 digit"
        
        # validate country    
        country=data.get('country', None)
        if country is not None:
            country=country.strip()
            if not all(word.isalpha() for word in country.split()):
                errors['country']='Country name must be Character'
        
        # validate phone
        phone=data.get('phone')
        if phone is not None:
            if len(str(phone)) !=10:
                errors['phone']='phone number must be 10 digit'

        # validate email
        email=data.get('email', None)
        if email is not None:
            email=email.strip()
            if not email.endswith('@gmail.com'):
                errors['email']='email should endwith @gmail.com'
            
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
    
    def validate(self, data):
        errors={}
        
        # validate account number
        account_number=data.get('account_number', None)
        if account_number is not None:
            if len(str(account_number)) !=14:
                errors['account_number']='Account number should exactaly 14 digit.'
                
        # Validate balance
        balance = data.get('balance', None)
        if balance is not None:
            if  balance < 0: # OR if not isinstance(balance, (int, float)) or balance < 0:
                errors['balance'] = "Amount should be a positive number."
        
        if errors:
            raise serializers.ValidationError(errors)
        return data
    
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
    
    # Here validating all fields of AccountHolder
    def validate(self, data):
        
        errors={}
        
        holder_name=data.get('holder_name', None)
        if holder_name is not None:
            holder_name=holder_name.strip()
            if not all(word.isalpha() for word in holder_name.split()):
                errors['holder_name']='Name should be character'
            
        # Validate DOB (choose DOB who has complete 18 yrs from today date)
        date_of_birth = data.get('date_of_birth', None)
        if date_of_birth is not None:
            if date_of_birth:
                if date_of_birth > date.today():
                    errors['date_of_birth'] = 'Date of birth cannot be in the future'
                elif date_of_birth > date.today() - timedelta(days=18*365):
                    errors['date_of_birth'] = 'Account holder must be at least 18 years old'
                    
        father_name=data.get('father_name', None)
        if father_name is not None:
            father_name=father_name.strip()
            if not all(word.isalpha() for word in father_name.split()):
                errors['father_name']='Name should be character'
                
        mother_name=data.get('mother_name', None)
        if mother_name is not None:
            mother_name=mother_name.strip()    
            if not all(word.isalpha() for word in mother_name.split()):
                errors['mother_name']='Name should be character'
                
        qualification=data.get('qualification', None)
        if qualification is not None:
            qualification=qualification.strip()    
            if not all(word.isalpha() for word in qualification.split()):
                errors['qualification']='qualification should be character'
                
        address=data.get('address', None)
        if address is not None:
            address=address.strip()    
            if address.isdigit():
                errors['address']="address can't only Digit"
                
        city=data.get('city', None)
        if city is not None:
            city=city.strip()
            if not all(word.isalpha() for word in city.split()):
                errors['city']='Name should be character'
                
        pincode=data.get('pincode', None) 
        if pincode is not None:    
            if len(str(pincode)) !=6 or pincode < 0:
                errors['pincode']='pincode should be 6 digit'
                
        state=data.get('state', None)
        if state is not None:
            state=state.strip()
            if not all(word.isalpha() for word in state.split()):
                errors['state']='Name should be character'
                
        country=data.get('country', None)
        if country is not None:
            country=country.strip()
            if not all(word.isalpha() for word in country.split()):
                errors['country']='Name should be character'
            
        phone=data.get('phone', None)
        if phone is not None:
            if len(str(phone)) !=10:
                errors['phone']='Phone number should be 10 digit.'
                
        email=data.get('email', None)
        if email is not None:
            email=email.strip()
            if not email.endswith("@gmail.com"):
                errors['email']='email must be endwith @gmail.com.'
            
        if errors:
            raise serializers.ValidationError(errors)
        
        return data    
    
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
        
    def validate(self, data):
        errors = {}

        amount = data.get('amount', None)
        if amount is not None:
            if amount <= 0 or not isinstance(amount, (int, float, decimal.Decimal)):
                errors['amount'] = "Amount should be a positive number."

        account = data.get('account_number')
        if account and data['transaction_type'] == 'Withdraw' and account.balance < data['amount']:
            errors['amount'] = "Insufficient balance."

        if errors:
            raise serializers.ValidationError(errors)
        return data
    
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
