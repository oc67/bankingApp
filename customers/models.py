
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class Customers(AbstractUser):
    CustomerID=models.AutoField(primary_key=True,null=False,blank=False)

    #AccountID=models.ForeignKey(Accounts,null=True,blank=True,on_delete=models.CASCADE)


    FirstName=models.CharField(max_length=100,null=True,blank=True)
    MiddleName=models.CharField(max_length=100,null=True,blank=True)
    LastName=models.CharField(max_length=100,null=True,blank=True)
    NInumber=models.CharField(max_length=8,null=True,blank=True)
    Birthday=models.DateField(null=True,blank=True)
    Nationality=models.CharField(max_length=100,null=True,blank=True)
    CountryOfResidence=models.CharField(max_length=100,null=True,blank=True)
    Municipality=models.CharField(max_length=100,null=True,blank=True)
    StreetName=models.CharField(max_length=255,null=True,blank=True)
    StreetNumber=models.IntegerField(null=True,blank=True)
    Postcode=models.CharField(max_length=50,null=True,blank=True)
    AccountStatus=models.CharField(max_length=20,null=True,blank=True)
    CurrentSubscription=models.CharField(max_length=20,null=True,blank=True)
    JoiningDate=models.DateField(null=True,blank=True)
    EmploymentStatus = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        choices=(
        ('Self-employed', 'Self-employed'),
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Zero-hours', 'Zero-hours'),
        ('Student', 'Student'),
        ('Unemployed', 'Unemployed'),
        ('Retired', 'Retired'),
    )
)

    IncomeBand = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        choices=(
        ('£0-£10,000', '£0-£10,000'),
        ('£10,001-£30,000', '£10,001-£30,000'),
        ('£30,001-£50,000', '£30,001-£50,000'),
        ('£50,001-£100,000', '£50,001-£100,000'),
        ('£100,000+', '£100,000+'),
    )
)

    Industry = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        choices=(
        ('Agriculture', 'Agriculture'),
        ('Healthcare', 'Healthcare'),
        ('Apparel', 'Apparel'),
        ('Hospitality', 'Hospitality'),
        ('Banking', 'Banking'),
        ('Insurance', 'Insurance'),
        ('Biotechnology', 'Biotechnology'),
        ('Machinery', 'Machinery'),
        ('Chemicals', 'Chemicals'),
        ('Manufacturing', 'Manufacturing'),
        ('Communications', 'Communications'),
        ('Media', 'Media'),
        ('Construction', 'Construction'),
        ('Medical Device', 'Medical Device'),
        ('Consulting', 'Consulting'),
        ('Not For Profit', 'Not For Profit'),
        ('Education', 'Education'),
        ('Other', 'Other'),
        ('Electronics', 'Electronics'),
        ('Recreation', 'Recreation'),
        ('Energy', 'Energy'),
        ('Retail', 'Retail'),
        ('Engineering', 'Engineering'),
        ('Shipping', 'Shipping'),
        ('Entertainment', 'Entertainment'),
        ('Technology', 'Technology'),
        ('Environmental', 'Environmental'),
        ('Telecommunications', 'Telecommunications'),
        ('Finance', 'Finance'),
        ('Transportation', 'Transportation'),
        ('Food & Beverage', 'Food & Beverage'),
        ('Utilities', 'Utilities'),
        ('Government', 'Government'),
    )
)

    ExperianCreditRating=models.IntegerField(null=True,blank=True)
    RiskCategory=models.CharField(null=True,blank=True,max_length=10,choices=(('Low','Low'),('Medium','Medium'),('High','High')))



    def __str__(self):#
        return str(self.CustomerID)

