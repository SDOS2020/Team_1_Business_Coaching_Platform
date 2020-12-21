from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import CoachCreationForm, CoacheeCreationForm, UserPasswordChangeForm
from .decorators import is_coach, is_coachee, requested_user_is_coach_or_connection
from .models import Coach, Coachee, CustomUser, Connection
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework import viewsets
from .serializer import ConnectionSerializer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView


class ConnectionViewSet(viewsets.ViewSet):
    """
        A viewset for viewing and editing connection instances.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        if request.user.is_coach:
            connections = Connection.objects.filter(coach_id = request.user.coach.id)
            serializer = ConnectionSerializer(connections, many = True)
            return Response(serializer.data)
        if request.user.is_coachee:
            connections = Connection.objects.filter(coachee_id = request.user.coachee.id)
            serializer = ConnectionSerializer(connections, many = True)
            return Response(serializer.data)
        return Response([], status = status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        user_coach = CustomUser.objects.get(pk = request.data['pk'])
        if user_coach.is_coach and request.user.is_coachee and (Connection.objects.filter(coach = user_coach.coach, coachee = request.user.coachee).exists() == False):
            connection = Connection.objects.create(coach = user_coach.coach, coachee = request.user.coachee, accepted = False)
            serializer = ConnectionSerializer(connection)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response([], status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk = None):
        requested_user = get_object_or_404(CustomUser, pk = pk)
        if request.user.is_coach and requested_user.is_coachee and Connection.objects.filter(coach_id = request.user.coach.id, coachee = requested_user.coachee).exists():
            connection = get_object_or_404(Connection, coach_id = request.user.coach.id, coachee = requested_user.coachee)
            serializer = ConnectionSerializer(connection)
            return Response(serializer.data)
        if request.user.is_coachee and requested_user.is_coach and Connection.objects.filter(coachee_id = request.user.coachee.id, coach = requested_user.coach).exists():
            connection = get_object_or_404(Connection, coachee_id = request.user.coachee.id, coach = requested_user.coach)
            serializer = ConnectionSerializer(connection)
            return Response(serializer.data)
        return Response([], status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk = None):
        if request.user.is_coach and request.user.coach.id == request.data['coach']['id'] and pk:
            connection = Connection.objects.get(pk = pk, coach = request.user.coach)
            connection.accepted = True
            connection.save()
            serializer = ConnectionSerializer(connection)
            return Response(serializer.data)
        return Response([], status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk = None):
        if request.user.is_coach and request.user.coach.id == request.data['coach']['id'] and pk:
            connection = Connection.objects.get(pk = pk, coach = request.user.coach)
            connection.delete()
            serializer = ConnectionSerializer(connection)
            return Response(serializer.data)
        return Response([], status = status.HTTP_400_BAD_REQUEST)


class CoachRegisterView(CreateView):
    form_class = CoachCreationForm
    success_url = reverse_lazy('login')
    template_name = 'user/register_coach.html'


class CoacheeRegisterView(CreateView):
    form_class = CoacheeCreationForm
    success_url = reverse_lazy('login')
    template_name = 'user/register_coachee.html'


class CoachUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    success_url = reverse_lazy('dashboard')
    template_name = 'user/update_coach.html'
    model = Coach
    fields = ['first_name', 'last_name', 'area_of_expertise', 'profile_photo', 'linkedin','location','description' , 'coaching_hours']

    def test_func(self):
        coach = self.get_object()
        if self.request.user.coach == coach:
            return True
        return False


class CoacheeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
    success_url = reverse_lazy('dashboard')
    template_name = 'user/update_coachee.html'
    model = Coachee
    fields = ['first_name', 'last_name', 'profile_photo', 'linkedin','location','resume','purpose','contact']

    def test_func(self):
        coachee = self.get_object()
        if self.request.user.coachee == coachee:
            return True
        return False

class ChangeUserPasswordView(PasswordChangeView):
    template_name = 'user/change_password.html'
    success_url = reverse_lazy('login')
    form_class = UserPasswordChangeForm


@requested_user_is_coach_or_connection
@login_required
def profile(request, pk = None):
    requested_user = get_object_or_404(CustomUser, pk = pk)
    if requested_user.is_coach and request.user == requested_user:
        return render(request, 'user/profile_coach.html', {'profile' : requested_user})

    elif requested_user.is_coach:
        return render(request, 'user/profile_coach_view.html', {'profile' : requested_user})

    elif requested_user.is_coachee and request.user == requested_user:
        return render(request, 'user/profile_coachee.html', {'profile' : requested_user})

    elif requested_user.is_coachee and request.user.is_coach and connection_exists(request.user, requested_user):
        return render(request, 'user/profile_coachee.html', {'profile' : requested_user})

    else:
        return redirect('home')


def connection_exists(user1, user2):
    if user1.is_coach and user2.is_coachee and (Connection.objects.filter(coach = user1.coach, coachee = user2.coachee, accepted = True).exists()):
        return True
    if user2.is_coach and user1.is_coachee and (Connection.objects.filter(coach = user2.coach, coachee = user1.coachee, accepted = True).exists()):
        return True
    return False

def get_connection(user1, user2):
    """
        Returns the Connection object connecting user1 and user2
    """
    if user1.is_coach and user2.is_coachee:
        connection = Connection.objects.filter(coach=user1.coach, coachee=user2.coachee, accepted=True)
        if connection.exists():
            return connection.first()
    if user2.is_coach and user1.is_coachee:
        connection = Connection.objects.filter(coach=user2.coach, coachee=user1.coachee, accepted=True)
        if connection.exists():
            return connection.first()
    return None

def get_all_connections(user):
    if user.is_coach:
        return Connection.objects.filter(coach = user.coach, accepted = True)
    else:
        return Connection.objects.filter(coachee = user.coachee, accepted = True)
