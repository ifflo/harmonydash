from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


# Similarly, create views for other models/endpoints
