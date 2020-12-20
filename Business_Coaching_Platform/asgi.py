"""
ASGI config for Business_Coaching_Platform project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from django.conf.urls import url
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Business_Coaching_Platform.settings")
django_asgi_app = get_asgi_application()

from django.urls import re_path
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from notification.consumers import NotificationConsumer

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter([
            re_path(r"^ws/notification/$", NotificationConsumer.as_asgi()),
        ])
    ),
    'channel': ChannelNameRouter(
        {
            'NotificationConsumerRoute': NotificationConsumer
        }
    ),
})