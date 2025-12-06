from django.db import models
from loans.models import Loan

# Create your models here.
class Repayment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='repayments')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['payment_date']

    def __str__(self):
        return f"Repayment of {self.amount_paid} on Loan {self.loan.id}"