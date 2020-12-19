from django.db import models
from user.models import CustomUser

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    event = models.CharField(max_length = 50)