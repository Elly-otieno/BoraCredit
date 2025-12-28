from rest_framework import serializers
from .models import Loan

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['id', 'user', 'principal_amount', 'max_interest_rate', 'early_repayment_discount_rate', 'issue_date', 'due_date', 'status', 'current_balance' ]
        read_only_fields = ['user', 'status', 'issue_date', 'current_balance', 'max_interest_rate']

