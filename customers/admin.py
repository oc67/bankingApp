from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Customers
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=Customers
    list_display=[
        "CustomerID",
        #"username",  
        #"email",
        "FirstName",
        "MiddleName",
        "LastName",
        "NInumber",
        "Birthday",
        "Nationality",
        "CountryOfResidence",
        "Municipality",
        "StreetName",
        "StreetNumber",
        "Postcode",
        "AccountStatus",
        "CurrentSubscription",
        "JoiningDate",
        "EmploymentStatus",
        "IncomeBand",
        "Industry",
        "ExperianCreditRating",
        "RiskCategory"
    ]
    fieldsets=UserAdmin.fieldsets+((None, {"fields":( 
           #"CustomerID",
           # "username",  
            #"email",
            "FirstName",
            "MiddleName",
            "LastName",
            "NInumber",
            "Birthday",
            "Nationality",
            "CountryOfResidence",
            "Municipality",
            "StreetName",
            "StreetNumber",
            "Postcode",
            "AccountStatus",
            "CurrentSubscription",
            "JoiningDate",
            "EmploymentStatus",
            "IncomeBand",
            "Industry",
            "ExperianCreditRating",
            "RiskCategory",)}),)
    add_fieldsets=UserAdmin.add_fieldsets+((None, {"fields":(
            #"CustomerID",
            "username",  
            "email",
            "FirstName",
            "MiddleName",
            "LastName",
            "NInumber",
            "Birthday",
            "Nationality",
            "CountryOfResidence",
            "Municipality",
            "StreetName",
            "StreetNumber",
            "Postcode",
            "AccountStatus",
            "CurrentSubscription",
            "JoiningDate",
            "EmploymentStatus",
            "IncomeBand",
            "Industry",
            "ExperianCreditRating",
            "RiskCategory",)}),)


admin.site.register(Customers, CustomUserAdmin)