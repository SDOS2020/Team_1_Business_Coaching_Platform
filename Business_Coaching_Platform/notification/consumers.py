import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from user.models import CustomUser
from django.shortcuts import get_object_or_404



class NotificationConsumer(WebsocketConsumer):
    
    def connect(self):
        user = get_object_or_404(CustomUser,  email = self.scope["user"])
        self.room_group_name = "group_" + str(user.pk)
        
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()


    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'notify',
                'message': message
            }
        )

    # Receive message from room group
    def notify(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))