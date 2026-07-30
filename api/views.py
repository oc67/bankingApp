from django.shortcuts import render
from rest_framework import generics

from transactions.models import Transactions
from .serializers import TransactionSerializer, CardSerializer, AccountSerializer
# Create your views here.

class TransactionAPIView(generics.ListAPIView):
    queryset=Transactions.objects.all()
    serializer_class=TransactionSerializer

class CardAPIView(generics.ListAPIView):
    queryset=Transactions.objects.all()
    serializer_class=CardSerializer


class AccountAPIView(generics.ListAPIView):
    queryset=Transactions.objects.all()
    serializer_class=AccountSerializer