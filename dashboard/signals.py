from django.dispatch import receiver
from django.db.models.signals import post_save
from dashboard.models import Chat
from notification.models import Notification

@receiver(post_save, sender = Chat)
def message_received(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(sender = instance.sender, event = "New Message", receiver = instance.receiver)