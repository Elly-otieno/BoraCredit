from rest_framework import serializers
from .models import Repayment

class RepaymentSerializer(serializers.ModelSerializers):
    class Meta:
        model = Repayment
        fields = ['id', 'loan', 'amout_paid', 'payment_date' ]