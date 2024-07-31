from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from bankapp.models import Bank, Branch, Account, AccountHolder, Transaction
from bankapp.serializers import BankSerializer, BranchSerializer, AccountSerilizer, AccountHolderSerializer, TransactionSerializer
#from rest_framework.authentication import BasicAuthentication
#from rest_framework.permissions import IsAuthenticated

# Here Using only Class APIView from Rest_Framework
class BankAPI(APIView):
    """
    Bank API
    """
    def get(self, request, pk=None, format=None):  # Here format is optional in DRF
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
                bank_obj=Bank.objects.get(id=pk)
                serializer=BankSerializer(bank_obj, data=request.data, partial=True)
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
                bank_obj=Bank.objects.get(id=pk)
                bank_obj.delete()
                return Response({"response":{"status":200,"message":"Bank Data has been deleted"}}, status=status.HTTP_200_OK)
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
                return Response({"response":{"status":200,"message":"Branch Data has been deleted"}}, status=status.HTTP_200_OK)
            except Branch.DoesNotExist:
                return Response ({"response":{"status":404,"error":"ID Doesn't Exist"}}, status=status.HTTP_404_NOT_FOUND)
        return Response({"response":{"status":400, "error":"please provide ID"}}, status=status.HTTP_400_BAD_REQUEST)
    
# Here Create Custome or Filter APIs Get single bank with all/signle Branch
class BankBranchAPIView(APIView):
    def get(self, request, pk=None, branch_pk=None): # Here having 2 pks, pk is bank id and branch_pk is branch id
        
        try:
            bank = Bank.objects.get(id=pk)
        except Bank.DoesNotExist:
            return Response({"response":{"status":404,"errors":"Bank ID doesn't exist."}}, status=status.HTTP_404_NOT_FOUND)
        
        if branch_pk is None: 
            branch = Branch.objects.filter(bank = bank) # Here get single Bank with all branch
            serializer_class = BranchSerializer(branch, many = True)
            return Response({"response":{"status":200,"payload":serializer_class.data}}, status = status.HTTP_200_OK)
        try:
            branch = Branch.objects.get(id=branch_pk, bank=bank)
            serializer_class = BranchSerializer(branch)
            return Response({"response":{"status":200, "payload":serializer_class.data}}, status=status.HTTP_200_OK)
        except Branch.DoesNotExist:
            return Response({"response":{"status":404,"errors":"Branch ID doen't exist."}}, status=status.HTTP_404_NOT_FOUND)
     
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
                return Response({"response":{"status":200,"message":"Account Data has been deleted"}}, status=status.HTTP_200_OK)
            except Account.DoesNotExist:
                return Response ({"response":{"status":404,"error":"ID Doesn't Exist"}}, status=status.HTTP_404_NOT_FOUND)
        return Response({"response":{"status":400, "error":"please provide ID"}}, status=status.HTTP_400_BAD_REQUEST)

# Here Create Custome API Filter Single Branch with All Accounts and single account
class BranchAccountAPIView(APIView):
    """
    SingleBranch-AllAccounts OR SingleBranch-SingleAccount APIs
    """
    def get(self, request, pk=None, acc_pk=None):
        # Check if the branch exists
        try:
            branch = Branch.objects.get(id=pk)
        except Branch.DoesNotExist:
            return Response({"response": {"status": 404, "errors": "Branch ID doesn't exist."}}, status=status.HTTP_404_NOT_FOUND)
        
        # Fetch accounts based on whether acc_pk is provided or not
        if acc_pk is None:
            # Fetch all accounts for the branch
            accounts = Account.objects.filter(branch=branch)
            serializer = AccountSerilizer(accounts, many=True)
            return Response({"response": {"status": 200, "payload": serializer.data}}, status=status.HTTP_200_OK)
        
        # Fetch a specific account for the branch
        try:
            account = Account.objects.get(id=acc_pk, branch=branch)
            serializer = AccountSerilizer(account)
            return Response({"response": {"status": 200, "data": serializer.data}}, status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            return Response({"response": {"status": 404, "errors": "Account ID doesn't exist."}}, status=status.HTTP_404_NOT_FOUND)
            
class AccountHolderAPI(APIView):
    """
    AccountHolder API
    """
    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                bank_object=AccountHolder.objects.get(id=pk)
                serializer=AccountHolderSerializer(bank_object)
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
                return Response({"response":{"status":200,"message":"Account Holder Data has been deleted"}}, status=status.HTTP_200_OK)
            except AccountHolder.DoesNotExist:
                return Response ({"response":{"status":404,"error":"ID Doesn't Exist"}}, status=status.HTTP_404_NOT_FOUND)
        return Response({"response":{"status":400, "error":"please provide ID"}}, status=status.HTTP_400_BAD_REQUEST)

# Here Create Holder with Account APIs like Holder/id/account or/account/id

class HolderAccountAPIView(APIView):
    """
    AccountHolder and Account APIs
    """
    def get(self, request, pk=None, acc_pk=None):
        
        try:
            accountholder = AccountHolder.objects.get(id=pk) 
        except AccountHolder.DoesNotExist:
            return Response({"response":{"status":404, "errors":"Account holder ID doesn't exist."}}, status=status.HTTP_404_NOT_FOUND)
        
        if acc_pk is None:
            account = Account.objects.filter(accountholder=accountholder)
            serializers_class = AccountSerilizer(account, many=True) 
            return Response({"response":{"status":200, "payload":serializers_class.data}}, status=status.HTTP_200_OK)
        try:
            account = Account.objects.get(id=acc_pk)
            serializers_class = AccountSerilizer(account) 
            return Response({"response":{"status":200, "payload":serializers_class.data}}, status=status.HTTP_200_OK) 
        except Account.DoesNotExist:
            return Response({"response":{"status":404, "errors":"Account ID doesn't exist."}}, status=status.HTTP_404_NOT_FOUND)
        
class TransactionAPI(APIView):
    """
    Transaction API
    """
    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                model=Transaction.objects.get(id=pk)
                serializer=TransactionSerializer(model)
                return Response({"response":{"status":200,"message":serializer.data}}, status=status.HTTP_200_OK)  
            except Transaction.DoesNotExist:
                return Response({"response":{"status":404,"error":"Id doesn't exist"}}, status=status.HTTP_404_NOT_FOUND)
                
        queryset=Transaction.objects.all()
        serializer=TransactionSerializer(queryset, many=True)
        return Response({"response":{"status":200,"message":serializer.data}}, status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({"response": {"status": 200, "message": "Data inserted successfully", "data": serializer.data}}, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"response": {"status": 400, "errors": str(e)}}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"response": {"status": 400, "errors": serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
    
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
                return Response({"response":{"status":200,"message":"transaction Data has been deleted"}}, status=status.HTTP_200_OK)
            except Transaction.DoesNotExist:
                return Response ({"response":{"status":404,"error":"ID Doesn't Exist"}}, status=status.HTTP_404_NOT_FOUND)
        return Response({"response":{"status":400, "error":"please provide ID"}}, status=status.HTTP_400_BAD_REQUEST)
    
# Here Create Custome API for Account with Transactions
class AccountTransactionAPIView(APIView):
    """
    Account and Transaction APIs
    """
    def get(self, request, pk=None, trans_pk=None, format=None):
        # Check if the account exists
        try:
            account = Account.objects.get(id=pk)
        except Account.DoesNotExist:
            return Response({"response": {"status": 404, "errors": "Account ID doesn't exist."}}, status=status.HTTP_404_NOT_FOUND)
        
        # Fetch transactions based on whether trans_pk is provided or not
        if trans_pk is None:
            # Fetch all transactions for the account
            transactions = Transaction.objects.filter(account_number=account)
            serializer = TransactionSerializer(transactions, many=True)
            return Response({"response": {"status": 200, "payload": serializer.data}}, status=status.HTTP_200_OK)
        
        # Fetch a specific transaction for the account
        try:
            transaction = Transaction.objects.get(id=trans_pk, account_number=account)
            serializer = TransactionSerializer(transaction)
            return Response({"response": {"status": 200, "payload": serializer.data}}, status=status.HTTP_200_OK)
        except Transaction.DoesNotExist:
            return Response({"response": {"status": 404, "errors": "Transaction ID doesn't exist."}}, status=status.HTTP_404_NOT_FOUND)
