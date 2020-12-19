from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.models import Coach, Coachee, CustomUser, Connection
from .models import Chat
from rest_framework import viewsets
from .serializer import ChatSerializer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db.models import Q
from user.views import connection_exists, get_all_connections
import html
from notification.views import notify


# Create your views here.
@login_required
def dashboard(request):
    if request.user.is_coach:
        return render(request, 'dashboard/coach_dashboard.html', {'profile' : request.user})
    elif request.user.is_coachee:
        return render(request, 'dashboard/coachee_dashboard.html', {'profile' : request.user})
    else:
        return redirect('home')


class ChatViewSet(viewsets.ViewSet):
    """
        A viewset for viewing and editing Chat instances.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        """
        Get chats between the authenticated user and all of his/her connections
        """
        connections = get_all_connections(request.user)
        chats = [ChatSerializer(get_chats_between_users(connection.coach.user, connection.coachee.user), many = True).data for connection in connections]
        return Response(chats)

    def retrieve(self, request, pk = None):
        """
        Get chats between the authenticated user and one of his/her connection (whose pk is specified)
        """
        other_user = get_object_or_404(CustomUser, pk = pk)
        if connection_exists(request.user, other_user):
            chats = get_chats_between_users(request.user, other_user)
            serializer = ChatSerializer(chats, many = True)
            return Response(serializer.data)
        return Response([], status = status.HTTP_400_BAD_REQUEST)
    
    def create(self, request):
        """
        Creates a chat message between authenticated user and one of his/her connection
        """
        other_user = get_object_or_404(CustomUser, pk = request.data['pk'])
        if connection_exists(request.user, other_user):
            chat = Chat.objects.create(sender = request.user, receiver = other_user, message = html.escape(request.data['message']))
            serializer = ChatSerializer(chat)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response([], status = status.HTTP_400_BAD_REQUEST)


def get_chats_between_users(user1, user2):
    """
    Returns all chat objects between 2 users sorted by date posted. 
    Note: It does not check if they are a connection
    """
    return Chat.objects.filter(Q(sender = user1, receiver = user2) | Q(sender = user2, receiver = user1)).order_by('-date_posted')
