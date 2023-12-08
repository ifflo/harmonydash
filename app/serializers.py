from rest_framework import serializers
from .models import UserProfile, Schedule, Task, FinancialSettings, Transaction  # Import your models
from .models import Salary, Bonus, Transaction

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


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = ['base_salary', 'payment_frequency', 'start_date', 'end_date']


class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = ['amount', 'date_received', 'reason', 'is_recurring']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['amount', 'date', 'transaction_type', 'category']
