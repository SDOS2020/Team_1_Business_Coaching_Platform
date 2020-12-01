from rest_framework import serializers
from .models import Chat
from user.serializer import CustomUserSerializer
from django.utils.timezone import now

class ChatSerializer(serializers.ModelSerializer):
    
    sender = CustomUserSerializer()
    receiver = CustomUserSerializer()
    time = serializers.SerializerMethodField('get_time')
    
    def get_time(self, chat):
        if chat.date_posted.strftime("%m/%d/%Y") == now().strftime("%m/%d/%Y"):
            return chat.date_posted.strftime("%H:%M")
        else:
            return chat.date_posted.strftime("%d/%m/%Y %H:%M")

    class Meta:
        model = Chat
        fields = ['pk', 'sender', 'receiver', 'message', 'time']