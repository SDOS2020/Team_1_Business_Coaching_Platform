from rest_framework import serializers
from .models import Notification
from user.serializer import CustomUserSerializer


class NotificationSerializer(serializers.ModelSerializer):
    sender = CustomUserSerializer()
    receiver = CustomUserSerializer()
    class Meta:
        model = Notification
        fields = ['pk', 'sender', 'receiver', 'event']