from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User

class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    full_name = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(write_only=True)
    address = serializers.CharField(write_only=True)
    national_id = serializers.CharField(write_only=True)
    employment_status = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'full_name', 'phone_number', 'address', 'national_id', 'employment_status']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Passwords do not match')
        return data
    
    def create(self, validated_data):
        # extract profile fields
        password = validated_data.pop('password')
        validated_data.pop('password2')
        full_name = validated_data.pop('full_name')
        phone_number = validated_data.pop('phone_number')
        address = validated_data.pop('address')
        national_id = validated_data.pop('national_id')
        employment_status = validated_data.pop('employment_status')

        # create user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=password
        )

        # create user profile
        UserProfile.objects.create(
            user=user,
            full_name=full_name,
            phone_number=phone_number,
            address=address,
            national_id=national_id,
            employment_status=employment_status
        )

        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'full_name', 'phone_number', 'address', 'national_id', 'employment_status' ]