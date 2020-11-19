from rest_framework import serializers
from .models import Coach, Coachee, Connection


class CoachSerializer(serializers.ModelSerializer):
    # Helps in Python to JSON conversion
    user_pk = serializers.SerializerMethodField('get_user_pk')

    def get_user_pk(self, coach):
        return coach.user.pk
        
    class Meta: 
        model = Coach
        fields = ['id', 'first_name', 'last_name',  'profile_photo', 'description','user_pk']


class CoacheeSerializer(serializers.ModelSerializer):
    # Helps in Python to JSON conversion
    user_pk = serializers.SerializerMethodField('get_user_pk')

    def get_user_pk(self, coachee):
        return coachee.user.pk

    class Meta: 
        model = Coachee
        fields = ['id', 'first_name', 'last_name', 'profile_photo','user_pk']


class ConnectionSerializer(serializers.ModelSerializer):
    coach = CoachSerializer()
    coachee = CoacheeSerializer()
    class Meta:
        model = Connection
        fields = ['pk', 'coach', 'coachee', 'accepted']