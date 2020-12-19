from django.conf import settings
from django.db import models
from django.utils import timezone
from user.serializer import CustomUserSerializer
from rest_framework import serializers

# noinspection PyUnresolvedReferences
from user.models import Coach, Coachee
# noinspection PyUnresolvedReferences
from user.serializer import CoachSerializer, CoacheeSerializer
from .models import Post
from django.utils.timezone import now

class PostSerializer(serializers.ModelSerializer):
    creator = CustomUserSerializer()
    viewer = CustomUserSerializer()
    date_posted = serializers.SerializerMethodField('get_time')

    def get_time(self, post):
        if post.date_posted.strftime("%m/%d/%Y") == now().strftime("%m/%d/%Y"):
            return post.date_posted.strftime("%I:%M %p")
        else:
            return post.date_posted.strftime("%d %B, %Y %I:%M %p")

    class Meta:
        model = Post
        fields = ['pk', 'creator','viewer','title','content','date_posted']