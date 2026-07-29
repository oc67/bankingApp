
from django.urls import path
from .views import TransactionAPIView

urlpatterns = [
    path("", TransactionAPIView.as_view()),

]
