
from django.urls import path
from .views import (TransactionListAPIView,AccountListAPIView,CardListAPIView,
                    TransactionDetailAPIView,AccountDetailAPIView,CardDetailAPIView)

urlpatterns = [
    path("transactions/", TransactionListAPIView.as_view()),

    path("transactions/<int:pk>/", TransactionDetailAPIView.as_view()),
    path("accounts/", AccountListAPIView.as_view()),
    path("accounts/<int:pk>/", AccountDetailAPIView.as_view()),

    path("cards/", CardListAPIView.as_view()),
    path("cards/<int:pk>/", CardDetailAPIView.as_view()),


]
