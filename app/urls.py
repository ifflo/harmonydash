# app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (FinancialSettingsViewSet, FinancialSummaryView, SalaryViewSet, BonusViewSet, TransactionViewSet,
                    MonthlyOverview, SpendingByCategory, TrendAnalysis)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'financial-settings', FinancialSettingsViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'salaries', SalaryViewSet)
router.register(r'bonuses', BonusViewSet)
router.register(r'all-transactions', TransactionViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('api/financial-summary/', FinancialSummaryView.as_view(), name='financial-summary'),
    path('api/monthly-overview/', MonthlyOverview.as_view(), name='monthly-overview'),
    path('api/spending-by-category/', SpendingByCategory.as_view(), name='spending-by-category'),
    path('api/trend-analysis/', TrendAnalysis.as_view(), name='trend-analysis'),
]
