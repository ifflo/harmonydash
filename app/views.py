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
