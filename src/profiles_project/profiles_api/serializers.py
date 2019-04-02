from rest_framework import serializers
from .models import UserProfile


class HelloSerializer(serializers.ModelSerializer):
    """Serializes a name field for testing APIView."""

    name = serializers.CharField(max_length=10)

    class Meta:
        model = UserProfile
        fields = ('name', )