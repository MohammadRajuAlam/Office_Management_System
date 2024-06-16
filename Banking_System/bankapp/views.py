from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from bankapp.models import Bank, Branch, Account, AccountHolder, Transaction
from bankapp.serializers import BankSerializer, BranchSerializer, AccountSerilizer, AccountHolderSerializer, TransactionSerializer

####  Here I am using only Class APIView from Rest_Framework

class BankAPI(APIView): 
    """
    Bank API
    """
    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                bank=Bank.objects.get(id=pk)
                serializer=BankSerializer(bank)
                return Response({"response":{"status":200,"payload":serializer.data}}, status=status.HTTP_200_OK)  
            except Bank.DoesNotExist:
                return Response({"response":{"status":404,"error":"Id doesn't exist"}}, status=status.HTTP_404_NOT_FOUND)    
        queryset=Bank.objects.all()
        serializer=BankSerializer(queryset, many=True)
        return Response({"response":{"status":200,"payload":serializer.data}}, status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer=BankSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response":{"status":200,"message":"Data inserted successfully","payload":serializer.data}}, status=status.HTTP_200_OK)
        return Response({"response":{"status":400,"errors":serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None, format=None):
        if pk is not None:
            try:
                queryset=Bank.objects.get(id=pk)
                serializer=BankSerializer(queryset, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"response":{"status":200,"message":"Bank data complete updated","payload":serializer.data}}, status=status.HTTP_200_OK)
                return Response({"response":{"status":400,"errors":serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
            except Bank.DoesNotExist:
                return Response({"response":{"status":404,"error":"ID Doesn't Exist"}}, status=status.HTTP_404_NOT_FOUND)
        return Response({"response":{"status":400,"error":"please provide ID"}}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk=None, format=None):
        if pk is not None:
            try:
                queryset=Bank.objects.get(id=pk)
                serializer=BankSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"response":{"status":200,"message":"Bank data Partial updated","payload":serializer.data}}, status=status.HTTP_200_OK)
                return Response({"response":{"status":400,"errors":serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
            except Bank.DoesNotExist:
                return Response({"response":{"status":404, "error":"ID Dosn't Exist"}}, status=status.HTTP_404_NOT_FOUND)
        return Response({"response":{"status":400,"error":"please provide ID"}}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk=None, format=None):
        if pk is not None:
            try:
                queryset=Bank.objects.get(id=pk)
                queryset.delete()
                return Response({"response":{"status":200,"message":"Bank Data has been deleted","payload":queryset}}, status=status.HTTP_200_OK)
            except Bank.DoesNotExist:
                return Response ({"response":{"status":404,"error":"ID Doesn't Exist"}}, status=status.HTTP_404_NOT_FOUND)
        return Response({"response":{"status":400, "error":"please provide ID"}}, status=status.HTTP_400_BAD_REQUEST)
    
class BranchAPI(APIView):
    """
    Branch API
    """
    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                branch=Branch.objects.get(id=pk)
                serializer=BranchSerializer(branch)
                return Response({"response":{"status":200,"message":serializer.data}}, status=status.HTTP_200_OK)  
            except Branch.DoesNotExist:
                return Response({"response":{"status":404,"error":"Id doesn't exist"}}, status=status.HTTP_404_NOT_FOUND)    
        queryset=Branch.objects.all()
        serializer=BranchSerializer(queryset, many=True)
        return Response({"response":{"status":200,"message":serializer.data}}, status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer=BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response":{"status":200,"message":"Data inserted successfully","payload":serializer.data}}, status=status.HTTP_200_OK)
        return Response({"response":{"status":400,"errors":serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None, format=None):
        if pk is not None:
            try:
                branch=Branch.objects.get(id=pk)
                serializer=BranchSerializer(branch, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"response":{"status":200,"message":"Branch data complete updated","payload":serializer.data}}, status=status.HTTP_200_OK)
                return Response({"response":{"status":400,"errors":serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
            except Branch.DoesNotExist:
                return Response({"response":{"status":404,"error":"ID Doesn't Exist"}}, status=status.HTTP_404_NOT_FOUND)
        return Response({"response":{"status":400,"error":"please provide ID"}}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk=None, format=None):
        if pk is not None:
            try:
                queryset=Branch.objects.get(id=pk)
                serializer=BranchSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"response":{"status":200,"message":"Branch data Partial updated","payload":serializer.data}}, status=status.HTTP_200_OK)
                return Response({"response":{"status":400,"errors":serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
            except Branch.DoesNotExist:
                return Response({"response":{"status":404, "error":"ID Dosn't Exist"}}, status=status.HTTP_404_NOT_FOUND)
        return Response({"response":{"status":400,"error":"please provide ID"}}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk=None, format=None):
        if pk is not None:
            try:
                queryset=Branch.objects.get(id=pk)
                queryset.delete()
                return Response({"response":{"status":200,"message":"Branch Data has been deleted","payload":queryset}}, status=status.HTTP_200_OK)
            except Branch.DoesNotExist:
                return Response ({"response":{"status":404,"error":"ID Doesn't Exist"}}, status=status.HTTP_404_NOT_FOUND)
        return Response({"response":{"status":400, "error":"please provide ID"}}, status=status.HTTP_400_BAD_REQUEST)
    
class AccountAPI(APIView):
    """
    Account API
    """
    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                account=Account.objects.get(id=pk)
                serializer=AccountSerilizer(account)
                return Response({"response":{"status":200,"message":serializer.data}}, status=status.HTTP_200_OK)  
            except Account.DoesNotExist:
                return Response({"response":{"status":404,"error":"Id doesn't exist"}}, status=status.HTTP_404_NOT_FOUND) 
               
        queryset=Account.objects.all()
        serializer=AccountSerilizer(queryset, many=True)
        return Response({"response":{"status":200,"message":serializer.data}}, status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer=AccountSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response":{"status":200,"message":"Data inserted successfully","data":serializer.data}}, status=status.HTTP_200_OK)
        return Response({"response":{"status":400,"errors":serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None, format=None):
        if pk is not None:
            try:
                branch=Account.objects.get(id=pk)
                serializer=AccountSerilizer(branch, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"response":{"status":200,"message":"Account data complete updated","data":serializer.data}}, status=status.HTTP_200_OK)
                return Response({"response":{"status":400,"errors":serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
            except Account.DoesNotExist:
                return Response({"response":{"status":404,"error":"ID Doesn't Exist"}}, status=status.HTTP_404_NOT_FOUND)
        return Response({"response":{"status":400,"error":"please provide ID"}}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk=None, format=None):
        if pk is not None:
            try:
                queryset=Account.objects.get(id=pk)
                serializer=AccountSerilizer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"response":{"status":200,"message":"Account data Partial updated", "data":serializer.data}}, status=status.HTTP_200_OK)
                return Response({"response":{"status":400,"errors":serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
            except Account.DoesNotExist:
                return Response({"response":{"status":404, "error":"ID Dosn't Exist"}}, status=status.HTTP_404_NOT_FOUND)
        return Response({"response":{"status":400,"error":"please provide ID"}}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk=None, format=None):
        if pk is not None:
            try:
                queryset=Account.objects.get(id=pk)
                queryset.delete()
                return Response({"response":{"status":200,"message":"Account Data has been deleted","dat":queryset}}, status=status.HTTP_200_OK)
            except Account.DoesNotExist:
                return Response ({"response":{"status":404,"error":"ID Doesn't Exist"}}, status=status.HTTP_404_NOT_FOUND)
        return Response({"response":{"status":400, "error":"please provide ID"}}, status=status.HTTP_400_BAD_REQUEST)
    
    
class AccountHolderAPI(APIView):
    """
    AccountHolder API
    """
    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                queryset=Bank.objects.get(id=pk)
                serializer=AccountHolderSerializer(queryset)
                return Response({"response":{"status":200,"message":serializer.data}}, status=status.HTTP_200_OK)  
            except AccountHolder.DoesNotExist:
                return Response({"response":{"status":404,"error":"Id doesn't exist"}}, status=status.HTTP_404_NOT_FOUND)    
        queryset=AccountHolder.objects.all()
        serializer=AccountHolderSerializer(queryset, many=True)
        return Response({"response":{"status":200,"message":serializer.data}}, status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer=AccountHolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response":{"status":200,"message":"Data inserted successfully","data":serializer.data}}, status=status.HTTP_200_OK)
        return Response({"response":{"status":400,"errors":serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None, format=None):
        if pk is not None:
            try:
                queryset=AccountHolder.objects.get(id=pk)
                serializer=AccountHolderSerializer(queryset, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"response":{"status":200,"message":"Account Hplder data complete updated","data":serializer.data}}, status=status.HTTP_200_OK)
                return Response({"response":{"status":400,"errors":serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
            except AccountHolder.DoesNotExist:
                return Response({"response":{"status":404,"error":"ID Doesn't Exist"}}, status=status.HTTP_404_NOT_FOUND)
        return Response({"response":{"status":400,"error":"please provide ID"}}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk=None, format=None):
        if pk is not None:
            try:
                queryset=AccountHolder.objects.get(id=pk)
                serializer=AccountHolderSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"response":{"status":200,"message":"Account Holder data Partial updated","data":serializer.data}}, status=status.HTTP_200_OK)
                return Response({"response":{"status":400,"errors":serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
            except AccountHolder.DoesNotExist:
                return Response({"response":{"status":404, "error":"ID Dosn't Exist"}}, status=status.HTTP_404_NOT_FOUND)
        return Response({"response":{"status":400,"error":"please provide ID"}}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk=None, format=None):
        if pk is not None:
            try:
                queryset=AccountHolder.objects.get(id=pk)
                queryset.delete()
                return Response({"response":{"status":200,"message":"Account Holder Data has been deleted","data":queryset}}, status=status.HTTP_200_OK)
            except AccountHolder.DoesNotExist:
                return Response ({"response":{"status":404,"error":"ID Doesn't Exist"}}, status=status.HTTP_404_NOT_FOUND)
        return Response({"response":{"status":400, "error":"please provide ID"}}, status=status.HTTP_400_BAD_REQUEST)
    
class TransactionAPI(APIView):
    """
    Transaction API
    """
    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                queryset=Transaction.objects.get(id=pk)
                serializer=TransactionSerializer(queryset)
                return Response({"response":{"status":200,"message":serializer.data}}, status=status.HTTP_200_OK)  
            except Transaction.DoesNotExist:
                return Response({"response":{"status":404,"error":"Id doesn't exist"}}, status=status.HTTP_404_NOT_FOUND)    
        queryset=Transaction.objects.all()
        serializer=Transaction(queryset, many=True)
        return Response({"response":{"status":200,"message":serializer.data}}, status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer=TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response":{"status":200,"message":"Data inserted successfully","data":serializer.data}}, status=status.HTTP_200_OK)
        return Response({"response":{"status":400,"errors":serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None, format=None):
        if pk is not None:
            try:
                queryset=Transaction.objects.get(id=pk)
                serializer=TransactionSerializer(queryset, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"response":{"status":200,"message":"Transaction data complete updated","data":serializer.data}}, status=status.HTTP_200_OK)
                return Response({"response":{"status":400,"errors":serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
            except Transaction.DoesNotExist:
                return Response({"response":{"status":404,"error":"ID Doesn't Exist"}}, status=status.HTTP_404_NOT_FOUND)
        return Response({"response":{"status":400,"error":"please provide ID"}}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk=None, format=None):
        if pk is not None:
            try:
                queryset=Transaction.objects.get(id=pk)
                serializer=TransactionSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"response":{"status":200,"message":"Transaction data Partial updated","data":serializer.data}}, status=status.HTTP_200_OK)
                return Response({"response":{"status":400,"errors":serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
            except Transaction.DoesNotExist:
                return Response({"response":{"status":404, "error":"ID Dosn't Exist"}}, status=status.HTTP_404_NOT_FOUND)
        return Response({"response":{"status":400,"error":"please provide ID"}}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk=None, format=None):
        if pk is not None:
            try:
                queryset=Transaction.objects.get(id=pk)
                queryset.delete()
                return Response({"response":{"status":200,"message":"transaction Data has been deleted","data":queryset}}, status=status.HTTP_200_OK)
            except Transaction.DoesNotExist:
                return Response ({"response":{"status":404,"error":"ID Doesn't Exist"}}, status=status.HTTP_404_NOT_FOUND)
        return Response({"response":{"status":400, "error":"please provide ID"}}, status=status.HTTP_400_BAD_REQUEST)