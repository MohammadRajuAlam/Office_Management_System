from django.contrib import admin
from django.urls import path
from bankapp.views import BankAPI, BranchAPI, BankBranchAPIView,AccountAPI,BranchAccountAPIView,AccountHolderAPI,HolderAccountAPIView,TransactionAPI, AccountTransactionAPIView

urlpatterns = [
    path('banks/', BankAPI.as_view(), name='BankAPI'), # Here Access/get All banks (We can do all HTTP operations)
    path('banks/<int:pk>/', BankAPI.as_view(), name='BankAPI'), # Here access/get a specific bank
    path('branch/', BranchAPI.as_view(), name='BranchAPI'),     # Here access All branches
    path('branch/<int:pk>/', BranchAPI.as_view(), name='BranchAPI'), # Here access a specific branch
    # Here custome URLs like bank/{bank_id}/branch
    path('banks/<int:pk>/branch/', BankBranchAPIView.as_view(), name="SingleBank-AllBranches"),
    path('banks/<int:pk>/branch/<int:branch_pk>/', BankBranchAPIView.as_view(), name='SingleBank-SingleBranch'),
    
    path('accounts/', AccountAPI.as_view(), name='AccountAPI'),     # Here access all accounts
    path('accounts/<int:pk>/', AccountAPI.as_view(), name='AccountAPI'), # Here access a specific account
    # Here custome URLs like Branch/{branch_id}/Accounts
    path("branch/<int:pk>/accounts/", BranchAccountAPIView.as_view(), name='SigleBranch-AllAccounts'),
    path("branch/<int:pk>/accounts/<int:acc_pk>/", BranchAccountAPIView.as_view(), name='SigleBranch-SingleAccounts'),
    path('accountholder/', AccountHolderAPI.as_view(), name='AccountHolderAPI'),  # Here access all account Holders
    path("accountholder/<int:pk>/", AccountHolderAPI.as_view(), name='AccountHolderAPI'),  # Here access a specific account Holder
    #Custome URLs like AccountHolder with Accounts
    path('accountholder/<int:pk>/accounts/', HolderAccountAPIView.as_view(), name="SingleAccountHolder-allAccounts"),
    path('accountholder/<int:pk>/accounts/<int:acc_pk>/', HolderAccountAPIView.as_view(), name="SingleAccountHolder-allAccounts"),
    path('transactions/', TransactionAPI.as_view(), name='TransactionAPI'),              # Here access all Transactions
    path('transactions/<int:pk>/', TransactionAPI.as_view(), name='TransactionAPI'),       # Here access a specific Transaction
    # Here Custome URLs account with transactions
    path('accounts/<int:pk>/transactions/', AccountTransactionAPIView.as_view(), name='account-transactions'),
    path('accounts/<int:pk>/transactions/<int:trans_pk>/', AccountTransactionAPIView.as_view(), name='account-transaction-detail'),
    
]