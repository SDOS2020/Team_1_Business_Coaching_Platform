from django.dispatch import receiver
from django.db.models.signals import post_save
from notification.models import Notification
from notification.views import notify


@receiver(post_save, sender = Notification)
def notification_received(sender, instance, created, **kwargs):
    notify(instance.receiver.pk, instance.event)

