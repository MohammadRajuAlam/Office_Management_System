from django.contrib import admin
from django.urls import path
from bankapp.views import BankAPI, BranchAPI, AccountAPI,AccountHolderAPI, TransactionAPI

urlpatterns = [
    path('banks/', BankAPI.as_view(), name='BankAPI'), # Here Access/get All banks (We can do all HTTP operations)
    path('banks/<int:pk>/', BankAPI.as_view(), name='BankAPI'), # Here access/get a specific bank
    path('branch/', BranchAPI.as_view(), name='BranchAPI'),     # Here access All branches
    path('branch/<int:pk>', BranchAPI.as_view(), name='BranchAPI'), # Here access a specific branch
    path('accounts/', AccountAPI.as_view(), name='AccountAPI'),     # Here access all accounts
    path('accounts/<int:pk>', AccountAPI.as_view(), name='AccountAPI'), # Here access a specific account
    path('accountholder/', AccountHolderAPI.as_view(), name='AccountHolderAPI'),  # Here access all account Holders
    path("accountholder/<int:pk>", AccountHolderAPI.as_view(), name='AccountHolderAPI'),  # Here access a specific account Holder
    path('transaction/', TransactionAPI.as_view(), name='TransactionAPI'),              # Here access all Transactions
    path('transaction/<int:pk>', TransactionAPI.as_view(), name='TransactionAPI'),       # Here access a specific Transaction
]