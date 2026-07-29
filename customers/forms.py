from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customers


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Customers
        fields = UserCreationForm.Meta.fields+("age",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Customers
        fields = UserChangeForm.Meta.fields

