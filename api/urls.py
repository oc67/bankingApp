
from django.urls import path
from .views import TransactionAPIView,AccountAPIView,CardAPIView

urlpatterns = [
    path("transactions/", TransactionAPIView.as_view()),
    path("accounts/", AccountAPIView.as_view()),
    path("cards/", CardAPIView.as_view()),

]
