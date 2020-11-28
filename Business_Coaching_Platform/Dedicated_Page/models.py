from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
import os
# print("PATH",os.getcwd())
# noinspection PyUnresolvedReferences
from user.models import Coach, Coachee


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    coach = models.ForeignKey(Coach, on_delete = models.CASCADE)
    coachee = models.ForeignKey(Coachee, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = "Posts"
