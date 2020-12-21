from user.models import Coach
from rest_framework.viewsets import ModelViewSet
from user.serializer import CoachSerializer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def find_coach(request):
    return render(request, 'enrolment/find_coach.html')

#a grid view of all coaches
class FindCoachViewSet(ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]