from django.db import models
from user.models import CustomUser

class Notification(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='receiver')
    event = models.CharField(max_length = 50)
