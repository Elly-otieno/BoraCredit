from django.db import models
from django.contrib.auth.models import User
from datetime import date
from decimal import Decimal

# Create your models here.

# ---ENUM & CHOICES ---
class LoanStatus(models.TextChoices):
    ACTIVE = 'active', ('Active')
    PAID = 'paid', ('Paid')
    OVERDUE = 'overdue', ('Overdue')
    DEFAULTED = 'defaulted', ('Defaulted')


class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loans')
    principal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    max_interest_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    early_repayment_discount_rate = models.DecimalField(max_digits=5, decimal_places=2)
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    status = models.CharField(
        choices=LoanStatus.choices,
        default=LoanStatus.ACTIVE,
        max_length=10
    )
    current_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def calculate_total_payable(self, repayment_date: date) -> Decimal:
        """
        Calculate total payable based on repayment day
        Day 1 = 1% interest, Day 2 = 2 % ..., capped at max_interest_rate.
        
        :param self: Description
        :param repayment_date: Description
        :type repayment_date: date
        :return: Description
        :rtype: Decimal
        """

        days_elapsed = (repayment_date - self.issue_date).days + 1
        interest_rate = Decimal(days_elapsed)

        interest_amount = self.principal_amount * (interest_rate/ Decimal(100))
        total_payable = self.principal_amount + interest_amount

        # early repayment discount
        if days_elapsed == 1 and self.early_repayment_discount_rate > 0:
            discount = self.principal_amount * (self.early_repayment_discount_rate / Decimal(100))
            total_payable -= discount

        return total_payable
    
    def total_repaid(self) -> Decimal:
        return sum(r.amount_paid for r in self.repayments.all())
    
    def outstanding_bal(self, repayment_date: date = None) -> Decimal:
        repayment_date = repayment_date or date.today()
        return self.calculate_total_payable(repayment_date) - self.total_repaid()

    def __str__(self):
        return f"Loan {self.id} for {self.user.username} - {self.status}"
