from user.models import Coach
from rest_framework.viewsets import ModelViewSet
from .serializers import CoachSerializer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


#a grid view of all coaches
class FindCoachViewSet(ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]