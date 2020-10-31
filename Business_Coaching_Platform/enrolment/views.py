from user.models import Coach
from rest_framework.viewsets import ModelViewSet
from .serializers import CoachSerializer


#a grid view of all coaches
class FindCoachViewSet(ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer

#Info about selected coach
class DisplayCoachViewSet(ModelViewSet):
    pass

#View for choosing slots for booking a free session
class FreeSessionViewSet(ModelViewSet):
    pass

#View for enrolling with a coach
class EnrolmentViewSet(ModelViewSet):
    pass