from django.db import models

# Here I am using python Class Model with Hard Delete, When we delete Root class models Objects, all class models objects references permanantly delete 
  
class Bank(models.Model):
    bank_name = models.CharField(max_length=100)
    bank_id = models.CharField(
        max_length=10,
        unique=True,
        error_messages={
            "unique": "Given bank_id is already used.",
        }
    )
    Bank_Types=(
        ('Goverment','Goverment'),
        ('Semi Goverment','Semi Goverment'),
        ('Private','Private'),
        ('Semi Private','Semi Private')
        ) # Here having 2 elements in tuple. First element represents value and stored in database and send element represents human-readable name displayed in forms or admin panels.
    bank_type=models.CharField(
        max_length=30,
        choices=Bank_Types
        )
    address=models.CharField(max_length=255)
    city=models.CharField(max_length=100)
    pincode=models.IntegerField()
    state=models.CharField(max_length=50)
    country=models.CharField(
        max_length=50,
        default='India'
        )
    phone=models.PositiveBigIntegerField(
        unique=True,
        error_messages={
        "unique":"Given phone number is already used"
        }
        ) # Here write customes errors
    email=models.EmailField(
        max_length=40,
        unique=True,
        error_messages={
            'unique': "This email id is already used."
            }
        )
    is_active=models.BooleanField(default=True)
    about=models.TextField(null=True, blank=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.bank_name}'
    
class Branch(models.Model):
    branch_name=models.CharField(max_length=100)
    branch_id=models.CharField(
        max_length=10,
        unique=True,
        error_messages={
            "unique":"Given Branch Id is already used."
            }
        )
    address=models.CharField(max_length=255)
    pincode=models.IntegerField()
    country=models.CharField(
        max_length=50,
        default='India'
        )
    phone=models.PositiveBigIntegerField(
        unique=True,
        error_messages={
            "unique":"Given Phone number is already used in Branch"
            }
    )
    email=models.EmailField(
        max_length=40,
        unique=True,
        error_messages={
            "unique":"Given Email ID is already used in Branch"
            }
        )
    is_active=models.BooleanField(default=True)
    bank=models.ForeignKey(Bank, on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.branch_name}'
    
class Account(models.Model):
    account_number=models.PositiveBigIntegerField(
        unique=True,
        error_messages={
            "unique":"account number is already exist"
        }
        )
    balance=models.FloatField(
        default=0
        )
    ACCOUNT_TYPES=(
        ('Saving','Saving'),
        ('Current','Current'),
        ('Joint', 'Joint')
        )
    account_type=models.CharField(
        max_length=30,
        choices=ACCOUNT_TYPES
        )
    branch=models.ForeignKey(Branch, on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    create_at=models.DateField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.account_number}'
    # OR 
    # def __str__(self):
    #     return str(self.account_number)
    
class AccountHolder(models.Model):
    holder_name=models.CharField(max_length=30)
    account_number=models.OneToOneField(Account, on_delete=models.CASCADE) # Here Hard Delete
    date_of_birth=models.DateField() # Here Need validation, Don't take future date for DOB
    father_name=models.CharField(max_length=30)
    mother_name=models.CharField(max_length=30)
    qualification=models.CharField(
        max_length=50,
        null=True,
        blank=True
        )
    address=models.CharField(max_length=255)
    city=models.CharField(max_length=50)
    pincode=models.IntegerField()
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50,default='India')
    phone=models.PositiveBigIntegerField()
    email=models.EmailField(
        max_length=40,
        unique=True,
        null=True,
        blank=True,
        error_messages={
            "unique":"Given Email id is already used."
            }
        )
    is_alive=models.BooleanField(default=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.holder_name}'
    
class Transaction(models.Model):
    account_number=models.ForeignKey(Account, on_delete=models.CASCADE) # Hard Delete
    TRANSACTION_TYPES=(
        ('Deposit','Deposit'),
        ('Withdraw','Withdraw')
        ) # Credit and Debit
    transaction_type=models.CharField(
        max_length=20, 
        choices=TRANSACTION_TYPES
        )
    amount=models.FloatField(default=0)
    transaction_date=models.DateTimeField(auto_now_add=True)
    
    # Here Create a function for Transaction the amount and update the balance
    def save(self, *args, **kwargs):
        if self.transaction_type == 'Deposit':
            self.account_number.balance += self.amount
        elif self.transaction_type == 'Withdraw':
            if self.account_number.balance < self.amount:
                raise ValueError("Insufficient balance")
            self.account_number.balance -= self.amount
        self.account_number.save()
        super(Transaction, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.transaction_type} {self.amount}'
    