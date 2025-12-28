from django.db import models
from loans.models import Loan
from django.core.exceptions import ValidationError

# Create your models here.
class Repayment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='repayments')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['payment_date']

    def __str__(self):
        return f"Repayment of {self.amount_paid} on Loan {self.loan.id}"
    
    def save(self, *args, **kwargs):

        if self.loan.status == LoanStatus.PAID:
            raise ValidationError("This loan is already fully paid.")

        super().save(*args, **kwargs)

        # update loan bal
        outstanding = self.loan.outstanding_bal(self.payment_date.date())
        self.loan.current_balalance = outstanding

        # update loan status
        if outstanding <= 0:
            self.loan.status = LoanStatus.PAID
        elif self.loan.due_date < self.payment_date.date() and outstanding > 0:
            self.loan.status = LoanStatus.OVERDUE

        self.loan.save()