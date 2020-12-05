from rest_framework import serializers
from .models import CustomUser, Coach, Coachee, Connection


class CustomUserSerializer(serializers.ModelSerializer):

    profile_photo = serializers.SerializerMethodField('get_profile_photo')
    name = serializers.SerializerMethodField('get_name')

    def get_profile_photo(self, user):
        if user.is_coach:
            return str(user.coach.profile_photo.url)
        elif user.is_coachee:
            return str(user.coachee.profile_photo.url)
    
    def get_name(self, user):
        if user.is_coach:
            return str(user.coach.first_name)
        elif user.is_coachee:
            return str(user.coachee.first_name)
         
    class Meta: 
        model = CustomUser
        fields = ['pk', 'profile_photo', 'name']


class CoachSerializer(serializers.ModelSerializer):

    user_pk = serializers.SerializerMethodField('get_user_pk')

    def get_user_pk(self, coach):
        return coach.user.pk
        
    class Meta: 
        model = Coach
        fields = ['id', 'first_name', 'last_name',  'profile_photo', 'description','user_pk']


class CoacheeSerializer(serializers.ModelSerializer):

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