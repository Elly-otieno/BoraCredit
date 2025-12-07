from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializers):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'full_name', 'phone_number', 'address', 'national_id', 'employment_status' ]