from django.contrib import admin
from django.urls import path
from bankapp.views import BankAPI, BranchAPI, AccountAPI,AccountHolderAPI, TransactionAPI

urlpatterns = [
    path('banks/<int:pk>', BankAPI.as_view(), name='BankAPI'),
    path('banks', BankAPI.as_view(), name='BankAPI'),
    path('branch/<int:pk>', BranchAPI.as_view(), name='BranchAPI'),
    path('branch/', BranchAPI.as_view(), name='BranchAPI'),
    path('accounts/<int:pk>', AccountAPI.as_view(), name='AccountAPI'),
    path('accounts', AccountAPI.as_view(), name='AccountAPI'),
    path("accountholder/<int:pk>", AccountHolderAPI.as_view(), name='AccountHolderAPI'),
    path('accountholder', AccountHolderAPI.as_view(), name='AccountHolderAPI'),
    path('transaction/<int:pk>', TransactionAPI.as_view(), name='TransactionAPI'),
    path('transaction', TransactionAPI.as_view(), name='TransactionAPI'),
]