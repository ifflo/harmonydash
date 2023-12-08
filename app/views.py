from rest_framework import generics, viewsets
from .models import UserProfile, FinancialSettings, Transaction
from .serializers import UserProfileSerializer, FinancialSettingsSerializer, TransactionSerializer


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
