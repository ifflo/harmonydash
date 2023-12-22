# app/views.py
from rest_framework import generics, viewsets
from .models import UserProfile, HomeFinancialSettings, UserSalary
from .serializers import (
    UserSalarySerializer,
    UserProfileSerializer,
    HomeFinancialSettingsSerializer
)
from django.http import JsonResponse
from django.views import View
from .utils.financial_analysis import analyze_transactions
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils.ynab_client import YNABClient
from django.conf import settings
import requests
from django.db.models import Sum, Q
from django.utils import timezone


# Existing ViewSets
class YNABProxyView(APIView):
    def get(self, request, endpoint, *args, **kwargs):
        ynab_client = YNABClient()
        try:
            budget_data = ynab_client.get_budgets()
            return Response(budget_data)
        except Exception as e:
            return Response({"error": str(e)}, status=400)


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class HomeFinancialSettingsViewSet(viewsets.ModelViewSet):
    queryset = HomeFinancialSettings.objects.all()
    serializer_class = HomeFinancialSettingsSerializer


# Newly added ViewSets
class UserSalaryViewSet(viewsets.ModelViewSet):
    queryset = UserSalary.objects.all()
    serializer_class = UserSalarySerializer


# Other views
class HomeFinancialDataView(View):
    def get(self, request, *args, **kwargs):
        # Assuming the user is authenticated and their ID is available
        user_id = request.user.id
        user = User.objects.get(pk=user_id)

        # Fetch and analyze transactions
        alerts = analyze_transactions(user)

        return JsonResponse({'alerts': alerts})


class HomeFinancialSummaryView(APIView):
    def get(self, request, format=None):
        # Your logic to gather financial summary data
        data = {'income': 1000, 'expenses': 500}  # Example data
        return Response(data)
