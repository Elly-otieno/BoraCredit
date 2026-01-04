from rest_framework import serializers
from .models import Loan
from repayment.serializers import RepaymentSerializer

class LoanSerializer(serializers.ModelSerializer):
    repayments = RepaymentSerializer(many=True, read_only=True)
    class Meta:
        model = Loan
        fields = ['id', 'user', 'principal_amount', 'max_interest_rate', 'early_repayment_discount_rate', 'issue_date', 'due_date', 'status', 'current_balance', 'repayments' ]
        read_only_fields = ['user', 'status', 'issue_date', 'current_balance', 'max_interest_rate']

# separate serializer for loan approval
class LoanApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['id', 'max_interest_rate', 'status']
        read_only_fields = ['id']