from django.conf import settings
from django.db import models
from django.utils import timezone
from rest_framework import serializers

# noinspection PyUnresolvedReferences
from user.models import Coach, Coachee
# noinspection PyUnresolvedReferences
from user.serializer import CoachSerializer, CoacheeSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    coach = CoachSerializer()
    coachee = CoacheeSerializer()
    class Meta:
        model = Post
        fields = ['title','content','date_posted']
