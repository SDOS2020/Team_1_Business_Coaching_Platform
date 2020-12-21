from django.conf import settings
from django.db import models
from django.utils import timezone
from user.serializer import CustomUserSerializer
from rest_framework import serializers
from rest_framework.parsers import FileUploadParser


# noinspection PyUnresolvedReferences
from user.models import Coach, Coachee
# noinspection PyUnresolvedReferences
from user.serializer import CoachSerializer, CoacheeSerializer
from .models import Post
from django.utils.timezone import now
from rest_framework.serializers import FileField, ListField


# Serializers define the API representation.
class UploadSerializer(serializers.Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']

# Serializer for multiple files upload.
class MultipleFilesUploadSerializer(serializers.Serializer):
    parser_classes = [FileUploadParser]
    file_uploaded = ListField(FileField())
    class Meta:
        fields = ['file_uploaded']


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
        fields = ['pk', 'creator','viewer','content','date_posted','uploaded_file_url','uploaded_file_name']
