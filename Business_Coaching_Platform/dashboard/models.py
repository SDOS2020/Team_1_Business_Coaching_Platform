from django.db import models
from user.models import CustomUser, Coach, Coachee
from django.utils.timezone import now


class Chat(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='chat_sender')
    receiver = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='chat_receiver')
    message = models.CharField(max_length = 300)
    date_posted = models.DateTimeField(default = now, editable = False)

    def __str__(self):
        return f"{self.sender} -> {self.receiver} : {self.message}"