from rest_framework import serializers

from transactions.models import Transactions
from accounts.models import Accounts
from cards.models import Cards



class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transactions
        fields=("TransactionID",
                "AccountID",
                "BankSortCode",
                "Amount",
                "Outcome",
                "RequestDate",
                "SettlementDate"

                )

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Accounts
        fields=(

                "AccountID", 
                "AccountType",
                "CustomerID",
            
                "SortCode",
            
                "BalanceInGBP",
            
                "CreditUsed",
                "CreditLimit",
                "AccruedReceivableInterestInGBP"

                )

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cards
        fields=(

         "CardID","CardType","AccountID","CustomerID","BespokeCashbackRatePayable","Status","ActivationDate","ExpirationDate"


                )