from rest_framework import serializers
from .models import Repayment

class RepaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repayment
        fields = ['id', 'loan', 'amount_paid', 'payment_date' ]
        read_only_fields = ['payment_date']

    def create(self, validate_data):
        repayment = super().create(validate_data)
        return repayment