from rest_framework import serializers
from .models import UserProfile, Schedule, Task  # Import your models


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

# Similarly, create serializers for other models
