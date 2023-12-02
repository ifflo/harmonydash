from django.urls import path
from . import views


urlpatterns = [
    path('api/userprofiles/', views.UserProfileList.as_view()),
    # Add more paths for other views
]