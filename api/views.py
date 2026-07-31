from django.shortcuts import render
from rest_framework import generics

from transactions.models import Transactions
from accounts.models import Accounts
from cards.models import Cards

from .serializers import TransactionSerializer, CardSerializer, AccountSerializer
# Create your views here.

class TransactionAPIView(generics.ListAPIView):
    queryset=Transactions.objects.all()#.filter(CustomerID= ) 
    serializer_class=TransactionSerializer

class CardAPIView(generics.ListAPIView):
    queryset=Cards.objects.all()#.filter(CardID= )
    serializer_class=CardSerializer


class AccountAPIView(generics.ListAPIView):
    queryset=Accounts.objects.all()#.filter(AccountID= )
    #queryset.filter()
    serializer_class=AccountSerializer