from django.shortcuts import render
from rest_framework import generics

from transactions.models import Transactions
from .serializers import TransactionSerializer
# Create your views here.

class TransactionAPIView(generics.ListAPIView):
    queryset=Transactions.objects.all()
    serializer_class=TransactionSerializer