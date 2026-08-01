from django.shortcuts import render
from rest_framework import generics, permissions

from transactions.models import Transactions
from accounts.models import Accounts
from cards.models import Cards

from .serializers import TransactionSerializer, CardSerializer, AccountSerializer

from .permissions import IsAuthor

# Create your views here.

class TransactionListAPIView(generics.ListCreateAPIView):
    #permission_classes=[IsAuthor]
    queryset=Transactions.objects.all()#.filter(CustomerID= ) 
    serializer_class=TransactionSerializer
    def get_queryset(self):
        return Transactions.objects.filter(AccountID__CustomerID=self.request.user)

class TransactionDetailAPIView(generics.RetrieveAPIView):
    #permission_classes=[IsAuthor]
    queryset=Transactions.objects.all()#.filter(CustomerID= ) 
    serializer_class=TransactionSerializer
    def get_queryset(self):
        return Transactions.objects.filter(AccountID__CustomerID=self.request.user)

    
class CardListAPIView(generics.ListCreateAPIView):
    #permission_classes=[IsAuthor]
    queryset=Cards.objects.all()#.filter(CardID= )
    serializer_class=CardSerializer
    def get_queryset(self):
        return Cards.objects.filter(CustomerID=self.request.user)

class CardDetailAPIView(generics.RetrieveAPIView):
    #permission_classes=[IsAuthor]
    queryset=Cards.objects.all()#.filter(CustomerID= ) 
    serializer_class=CardSerializer
    def get_queryset(self):
        return Cards.objects.filter(CustomerID=self.request.user)

class AccountListAPIView(generics.ListCreateAPIView):
    #permission_classes=[IsAuthor]
    queryset=Accounts.objects.all()#.filter(AccountID= )
    #queryset.filter()
    serializer_class=AccountSerializer
    def get_queryset(self):
        return Accounts.objects.filter(CustomerID=self.request.user)

class AccountDetailAPIView(generics.RetrieveAPIView):
    #permission_classes=[IsAuthor]
    queryset=Accounts.objects.all()#.filter(AccountID= )
    #queryset.filter()
    serializer_class=AccountSerializer
    def get_queryset(self):
        return Accounts.objects.filter(CustomerID=self.request.user)