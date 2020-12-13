from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
import os
# print("PATH",os.getcwd())
# noinspection PyUnresolvedReferences
from user.models import CustomUser,Coach, Coachee


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='post_creator')
    viewer = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='post_viewer')
    # post_file = models.FileField(null = True, blank = True, upload_to = 'post_files')
    uploaded_file_url = models.CharField(null=True, max_length=500)
    uploaded_file_name = models.CharField(null=True, max_length=500)
    def __str__(self):
        return f"{self.creator} -> {self.viewer} : {self.content}"

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = "Posts"