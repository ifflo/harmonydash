# app/views.py
from rest_framework import generics, viewsets
from .models import UserProfile, FinancialSettings, Transaction, Salary, Bonus
from .serializers import (
    SalarySerializer,
    BonusSerializer,
    TransactionSerializer,
    UserProfileSerializer,
    FinancialSettingsSerializer
)
from django.http import JsonResponse
from django.views import View
from .utils.financial_analysis import analyze_user_transactions
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from django.utils import timezone


# Existing ViewSets
class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class FinancialSettingsViewSet(viewsets.ModelViewSet):
    queryset = FinancialSettings.objects.all()
    serializer_class = FinancialSettingsSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


# Newly added ViewSets
class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer


class BonusViewSet(viewsets.ModelViewSet):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer


# Other views
class FinancialDataView(View):
    def get(self, request, *args, **kwargs):
        # Assuming the user is authenticated and their ID is available
        user_id = request.user.id
        user = User.objects.get(pk=user_id)

        # Fetch and analyze transactions
        alerts = analyze_user_transactions(user)

        return JsonResponse({'alerts': alerts})


class FinancialSummaryView(APIView):
    def get(self, request, format=None):
        # Your logic to gather financial summary data
        data = {'income': 1000, 'expenses': 500}  # Example data
        return Response(data)


class MonthlyOverview(APIView):
    def get(self, request, format=None):
        current_month = timezone.now().month
        total_income = Transaction.objects.filter(
            transaction_type='income', date__month=current_month
        ).aggregate(Sum('amount'))['amount__sum'] or 0
        total_expenses = Transaction.objects.filter(
            transaction_type='expense', date__month=current_month
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        data = {
            'income': total_income,
            'expenses': total_expenses
        }
        return Response(data)


class SpendingByCategory(APIView):
    def get(self, request, format=None):
        categories = (Transaction.objects.filter(transaction_type='expense')
                      .values('category').annotate(total=Sum('amount')).order_by('-total'))
        return Response(list(categories))


class TrendAnalysis(APIView):
    def get(self, request, format=None):
        trends = (Transaction.objects.values('date')
                  .annotate(income=Sum('amount',
                                       filter=Q(transaction_type='income')),
                            expenses=Sum('amount', filter=Q(transaction_type='expense'))).order_by('date'))
        return Response(list(trends))
