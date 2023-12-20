from django.test import TestCase
from app.models import Transaction, Salary, Bonus
from django.contrib.auth.models import User
from datetime import date
from decimal import Decimal


class SalaryBonusModelTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create(username='testuser')

        # Create a test salary entry
        Salary.objects.create(
            user=self.user,
            base_salary=50000,
            payment_frequency='monthly',
            start_date=date(2021, 1, 1),
            end_date=None  # Assuming this is an optional field
        )

        # Create a test bonus entry
        Bonus.objects.create(
            user=self.user,
            amount=3000,
            date_received=date(2021, 6, 15),
            reason='performance',
            is_recurring=False
        )

    def test_salary_creation(self):
        salary = Salary.objects.get(user=self.user)
        self.assertEqual(salary.base_salary, Decimal('50000'))

    def test_bonus_creation(self):
        bonus = Bonus.objects.get(user=self.user)
        self.assertEqual(bonus.amount, Decimal('3000'))


class FinancialAnalysisTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create(username='testuser')

        # Create sample transaction entries
        Transaction.objects.create(
            user=self.user,
            amount=150.00,
            date=date.today(),
            transaction_type='expense',
            category='Groceries'
        )

        Transaction.objects.create(
            user=self.user,
            amount=2000.00,
            date=date.today(),
            transaction_type='income',
            category='Salary'
        )
        # Add more transactions as needed for testing

    def test_calculate_monthly_expenses(self):
        expenses = calculate_monthly_expenses(self.user.id)
        self.assertTrue(len(expenses) > 0)
        # Additional assertions to validate the calculations

    def test_calculate_monthly_income(self):
        income = calculate_monthly_income(self.user.id)
        self.assertTrue(len(income) > 0)
        # Additional assertions

    def test_calculate_spending_by_category(self):
        spending = calculate_spending_by_category(self.user.id)
        self.assertTrue(len(spending) > 0)
        # Additional assertions
