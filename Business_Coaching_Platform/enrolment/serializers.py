from rest_framework.serializers import ModelSerializer
from user.models import Coach

class CoachSerializer(ModelSerializer):
    # Helps in Python to JSON conversion
    class Meta: 
        model = Coach
        fields = ['first_name', 'last_name', 'age']