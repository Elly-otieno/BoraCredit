from django.urls import path
from .views import RepaymentListCreateView, loan_repayments

urlpatterns = [
    path('repayments/', RepaymentListCreateView.as_view(), name='repayment-list'),
    path('loans/<int:pk>/repayments/', loan_repayments, name='loan-repayments')
]