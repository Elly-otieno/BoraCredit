from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

# ---ENUM & CHOICES ---
class LoanStatus(models.TextChoices):
    ACTIVE = 'active', ('Active')
    PAID = 'paid', ('Paid')
    OVERDUE = 'overdue', ('Overdue')
    DEFAULTED = 'defaulted', ('Defaulted')


class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loans')
    principal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    max_interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    early_repayment_discount_rate = models.DecimalField(max_digits=5, decimal_places=2)
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    status = models.CharField(
        choices=LoanStatus.choices,
        default=LoanStatus.ACTIVE,
        max_length=10
    )
    current_balalance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Loan {self.id} for {self.user.username} - {self.status}"
