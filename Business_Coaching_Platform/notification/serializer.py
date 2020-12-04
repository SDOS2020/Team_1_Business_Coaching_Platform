from rest_framework import serializers
from .models import Notification
from user.serializer import CustomUserSerializer


class NotificationSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    
    class Meta:
        model = Notification
        fields = ['pk', 'user', 'event']