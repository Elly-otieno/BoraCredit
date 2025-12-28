from django.urls import path
from .views import LoanApprovalView, LoanRequestView

urlpatterns = [
    path('request/', LoanRequestView.as_view(), name='loan-request'),
    path('loan/<int:pk>/approve/', LoanApprovalView.as_view(), name='loan-approve')
]