from django.shortcuts import render
from .serializers import RepaymentSerializer
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import PermissionDenied
from .models import Repayment
from loans.models import Loan
from loans.permissions import IsAdminUser

# Create your views here.

class RepaymentListCreateView(generics.ListCreateAPIView):
    serializer_class = RepaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        if IsAdminUser().has_permission(self.request, self):
            return Repayment.objects.all()
        return Repayment.objects.filter(loan__user=user)
    
    def perform_create(self, serializer):
        loan = serializer.validated_data['loan']
        if loan.user != self.request.user:
            raise PermissionDenied("You can only repay your own loans")
        serializer.save()

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def loan_repayments(request, pk):
    loan = Loan.objects.get(pk=pk, user=request.user)
    repayments = loan.repayments.all()
    serializer = RepaymentSerializer(repayments, many=True)
    return Response({
        "loan_id":loan.id,
        "principal":loan.principal_amount,
        "status":loan.status,
        "current_balance":loan.current_balance,
        "repayments":serializer.data
    }, status = status.HTTP_200_OK)

