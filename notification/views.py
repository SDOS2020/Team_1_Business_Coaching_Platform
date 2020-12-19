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


def room(request, room_name):
    return render(request, 'notification/room.html', {'room_name': room_name})


class NotificationViewSet(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        notifications = Notification.objects.filter(user = request.user)
        serializer = NotificationSerializer(notifications, many = True)
        return Response(serializer.data)

    def delete(self, request, pk = None):
        notification = get_object_or_404(Notification, pk = pk)
        if request.user == notification.user:
            notification.delete()
            serializer = NotificationSerializer(notification)
            return Response(serializer.data)
        return Response([], status.HTTP_400_BAD_REQUEST)


def notify(user_pk, message):
    group_name = "group_" + str(user_pk)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'notify',
            'message': message
        }
    )
