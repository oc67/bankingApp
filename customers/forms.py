from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customers


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Customers
        fields = UserCreationForm.Meta.fields+(
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
                "RiskCategory")

 

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Customers
        fields = UserChangeForm.Meta.fields

