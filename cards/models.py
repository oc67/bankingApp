from django.db import models
from customers.models import Customers
from accounts.models import Accounts


# Create your models here.

class Cards(models.Model):
    CardID=models.AutoField(primary_key=True,null=False,blank=False)
    #CardTypeID=models.BigIntegerField(null=False,blank=False)
    CardType=models.CharField(null=False,blank=False,choices=(('Credit','Credit'),('Debit','Debit')))

    AccountID=models.ForeignKey(Accounts,null=False,blank=False,on_delete=models.CASCADE)
    CustomerID=models.ForeignKey(Customers,null=False,blank=False,on_delete=models.CASCADE)


    BespokeCashbackRatePayable=models.DecimalField(decimal_places=5,max_digits=6,
                                            null=False,blank=False)

    Status=models.CharField(null=False,blank=False,choices=(('Inactive','Inactive'),('Inactive','Active'),
                                                            ('Frozen','Frozen'),('Expired','Expired')))
    ActivationDate=models.DateField(null=True,blank=True)
    ExpirationDate=models.DateField(null=True,blank=True)



    def __str__(self):
        return str(self.CardID)