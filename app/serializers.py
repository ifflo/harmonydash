from rest_framework import serializers
from .models import UserProfile, UserSchedule, UserSalary, HomeTasks, HomeFinancialSettings  # Import your models


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class HomeFinancialSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeFinancialSettings
        fields = '__all__'


class UserSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSalary
        fields = ['base_salary', 'payment_frequency', 'start_date', 'end_date']
