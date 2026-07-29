from rest_framework import serializers

from transactions.models import Transactions

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