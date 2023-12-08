# app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FinancialSettingsViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'financial-settings', FinancialSettingsViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
