# app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (HomeFinancialSettingsViewSet, UserSalaryViewSet, YNABProxyView)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'home-financial-settings', HomeFinancialSettingsViewSet)
router.register(r'user-salaries', UserSalaryViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('api/ynab/<str:endpoint>/', YNABProxyView.as_view(), name='ynab-proxy'),
]
