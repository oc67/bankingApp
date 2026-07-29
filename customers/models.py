
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Customers(AbstractUser):
    age=models.PositiveIntegerField(null=True,blank=True)
# AccountID=models.BigIntegerField(primary_key=True,null=False,blank=False)
# #AccountTypeID=models.BigIntegerField(null=False,blank=False)
# AccountType=models.CharField(null=False,blank=False,choices=(('Basic','Basic'),('Premium','Premium')))
#
# SortCode=models.CharField(max_length=8,null=False,blank=False) #requires validation: CHECK (SortCode LIKE '[0-9][0-9]-[0-9][0-9]-[0-9][0-9]')
#
# #For credit accounts, BalanceInGBP equals the credit available. For debit accounts, the field is just the balance
# BalanceInGBP=models.DecimalField(max_digits=10,decimal_places=2,null=False,blank=False)
#
# #Only for credit cards:
# CreditUsed=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
# CreditLimit=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
# AccruedReceivableInterestInGBP=models.DecimalField(decimal_places=4,max_digits=5,
#                                         null=False,blank=False)
#
#
#For savings accounts only:
# AccruedPayableInterestInGBP=models.DecimalField(decimal_places=4,max_digits=5,
#                                         null=False,blank=False)
#

#    def __str__(self):#
#        return self.AccountID