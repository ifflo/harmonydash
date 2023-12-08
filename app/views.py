from rest_framework import generics, viewsets
from .models import UserProfile, FinancialSettings, Transaction
from .serializers import UserProfileSerializer, FinancialSettingsSerializer, TransactionSerializer
from django.http import JsonResponse
from django.views import View
from .utils.financial_analysis import analyze_user_transactions
from django.contrib.auth.models import User


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class FinancialSettingsViewSet(viewsets.ModelViewSet):
    queryset = FinancialSettings.objects.all()
    serializer_class = FinancialSettingsSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
# Similarly, create views for other models/endpoints


class FinancialDataView(View):
    def get(self, request, *args, **kwargs):
        # Assuming the user is authenticated and their ID is available
        user_id = request.user.id
        user = User.objects.get(pk=user_id)

        # Fetch and analyze transactions
        alerts = analyze_user_transactions(user)

        return JsonResponse({'alerts': alerts})
