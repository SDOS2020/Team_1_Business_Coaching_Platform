from django.dispatch import receiver
from django.db.models.signals import post_save
from dedicated_page.models import Post
from notification.models import Notification

@receiver(post_save, sender = Post)
def post_received(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(sender = instance.creator, event = "New Post", receiver = instance.viewer)