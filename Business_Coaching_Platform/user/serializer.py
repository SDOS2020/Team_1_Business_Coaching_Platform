from rest_framework import serializers
from .models import Coach, Coachee, Connection


class CoachSerializer(serializers.ModelSerializer):
    # Helps in Python to JSON conversion
    class Meta: 
        model = Coach
        fields = ['id', 'first_name', 'last_name',  'profile_photo', 'description']


class CoacheeSerializer(serializers.ModelSerializer):
    # Helps in Python to JSON conversion
    class Meta: 
        model = Coachee
        fields = ['id', 'first_name', 'last_name', 'profile_photo']


class ConnectionSerializer(serializers.ModelSerializer):
    coach = CoachSerializer()
    coachee = CoacheeSerializer()
    class Meta:
        model = Connection
        fields = ['pk', 'coach', 'coachee', 'accepted']