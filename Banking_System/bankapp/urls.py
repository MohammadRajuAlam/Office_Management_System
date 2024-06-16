from django.contrib import admin
from django.urls import path
from bankapp.views import *  # BankAPI, BranchAPI, AccountAPI, TransactionAPI

urlpatterns = [
    path('banks/<int:pk>', BankAPI.as_view(), name='BankAPI'),
    path('banks', BankAPI.as_view(), name='BankAPI'),
    path('branch/<int:pk>', BranchAPI.as_view(), name='BranchAPI'),
    path('branch', BranchAPI.as_view(), name='BranchAPI'),
    path('account/<int:pk>', AccountAPI.as_view(), name='AccountAPI'),
    path('account', AccountAPI.as_view(), name='AccountAPI'),
    path("accountholder/<int:pk>", AccountHolderAPI.as_view(), name='AccountHolderAPI'),
    path('accountholder', AccountHolderAPI.as_view(), name='AccountHolderAPI'),
    path('transction/<int:pk>', TransactionAPI.as_view(), name='TransactionAPI'),
    path('transaction', TransactionAPI.as_view(), name='TransactionAPI'),
]