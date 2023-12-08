from rest_framework import serializers
from .models import UserProfile, Schedule, Task, FinancialSettings, Transaction  # Import your models


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class FinancialSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialSettings
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
# Similarly, create serializers for other models
