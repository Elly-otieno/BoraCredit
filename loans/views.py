from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Loan
from .serializers import LoanSerializer, LoanApprovalSerializer
from .permissions import IsAdminUser


# Create your views here.
class LoanRequestView(generics.CreateAPIView):
    serializer_class = LoanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, status="pending")


class LoanApprovalView(generics.UpdateAPIView):
    serializer_class = LoanApprovalSerializer
    queryset = Loan.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    def perform_update(self, serializer):
        serializer.save(status="Active")