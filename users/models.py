from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    address = models.TextField(max_length=400)
    national_id = models.CharField(max_length=50, unique=True)
    employment_status = models.CharField(max_length=100)

    def __str__(self):
        return f"Profile for {self.user.username}"