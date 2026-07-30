from django.db import models


# Create your models here.

class Transactions(models.Model):
    TransactionID=models.AutoField(primary_key=True,null=False,blank=False)

    #transaction row will only refer to one account: there should be two rows for trnasactions involving two clients of the bank.
    AccountID=models.BigIntegerField(null=False,blank=False)

    BankSortCode=models.CharField(max_length=8,null=False,blank=False) #requires validation: CHECK (SortCode LIKE '[0-9][0-9]-[0-9][0-9]-[0-9][0-9]')

    Amount=models.BigIntegerField(null=False,blank=False)
    Outcome=models.CharField(null=False,blank=False,choices=(('Pending','Pending'),('Complete','Complete'),
                                                    ('Failed','Failed')))
    RequestDate=models.DateField(null=False,blank=False)
    SettlementDate=models.DateField(null=True,blank=True)



    

    def __str__(self):
        return str(self.TransactionID)