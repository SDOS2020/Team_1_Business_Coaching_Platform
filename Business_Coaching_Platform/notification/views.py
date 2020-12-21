from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Notification
from .serializer import NotificationSerializer
from django.conf import settings 
from django.core.mail import send_mail 
from user.models import CustomUser

class NotificationViewSet(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        notifications = Notification.objects.filter(receiver = request.user)
        serializer = NotificationSerializer(notifications, many = True)
        return Response(serializer.data)

    def delete(self, request):
        pk = request.data['pk']
        notification = get_object_or_404(Notification, pk = pk)
        if request.user == notification.receiver:
            notification.delete()
            serializer = NotificationSerializer(notification)
            return Response(serializer.data)
        return Response([], status.HTTP_400_BAD_REQUEST)


def notify(user_pk, message):
    mail(user_pk, message)
    group_name = "group_" + str(user_pk)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'notify',
            'message': message
        }
    )

def mail(user_pk, message):
    user = CustomUser.objects.get(pk = user_pk)
    subject = 'Business Coaching Platform'
    body = f'{message}'
    email_from = settings.EMAIL_HOST_USER 
    recipient_list = [user.email, ]
    send_mail( subject, body, email_from, recipient_list ) 