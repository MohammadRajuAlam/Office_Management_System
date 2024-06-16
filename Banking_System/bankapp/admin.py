from django.contrib import admin
from bankapp.models import Bank, Branch, Account, AccountHolder, Transaction
# Register your models here.
#admin.site.register(Bank)
# OR
@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display=['id','bank_name','bank_id','address','city','pincode','state','country','phone','email','is_active','created_at','updated_at']

#admin.site.register(Branch)
#OR

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display=['id','branch_name','branch_id','address','pincode','country','phone','email','is_active','bank','created_at','update_at']
 
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display=['id','account_number','balance','account_type','branch','is_active','create_at','updated_at']
    
@admin.register(AccountHolder)
class AccountHolderAdmin(admin.ModelAdmin):
    list_display=['id','holder_name','account_number','date_of_birth','father_name','mother_name','qualification','address','city','pincode','state','country','phone','email','is_alive','created_at','updated_at']
    
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display=['id','account_number','transaction_type','amount','transaction_date']
