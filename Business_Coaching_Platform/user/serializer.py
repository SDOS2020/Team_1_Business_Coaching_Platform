from rest_framework import serializers
from .models import CustomUser, Coach, Coachee, Connection


class CustomUserSerializer(serializers.ModelSerializer):

    profile_photo = serializers.SerializerMethodField('get_profile_photo')
    name = serializers.SerializerMethodField('get_name')
    full_name = serializers.SerializerMethodField('get_full_name')

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

    def get_full_name(self,user):
        "Returns the person's full name."
        if user.is_coach:
            return '%s %s' % (user.coach.first_name, user.coach.last_name)
        elif user.is_coachee:
            return '%s %s' % (user.coachee.first_name, user.coachee.last_name)
    
    class Meta: 
        model = CustomUser
        fields = ['pk', 'profile_photo', 'name','full_name']


class CoachSerializer(serializers.ModelSerializer):

    user_pk = serializers.SerializerMethodField('get_user_pk')
    email = serializers.SerializerMethodField('get_email')

    def get_user_pk(self, coach):
        return coach.user.pk
    
    def get_email(self, coach):
        return coach.user.email

    class Meta: 
        model = Coach
        fields = ['id', 'first_name', 'last_name',  'profile_photo', 'description', 'user_pk', 'email']


class CoacheeSerializer(serializers.ModelSerializer):

    user_pk = serializers.SerializerMethodField('get_user_pk')
    email = serializers.SerializerMethodField('get_email')

    def get_user_pk(self, coachee):
        return coachee.user.pk

    def get_email(self, coachee):
        return coachee.user.email

    class Meta: 
        model = Coachee
        fields = ['id', 'first_name', 'last_name', 'profile_photo','user_pk', 'email']


class ConnectionSerializer(serializers.ModelSerializer):
    coach = CoachSerializer()
    coachee = CoacheeSerializer()

    # def get_coach_name(self,coach):
    #     name = coach.first_name+" "+coach.last_name
    #     return name
    #
    # def get_coachee_name(self,coachee):

    class Meta:
        model = Connection
        fields = ['pk', 'coach', 'coachee', 'accepted']