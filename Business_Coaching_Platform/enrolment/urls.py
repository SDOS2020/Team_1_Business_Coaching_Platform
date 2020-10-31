from django.urls import path
from rest_framework import routers
from .views import FindCoachViewSet

"""
REST framework adds support for automatic URL routing to Django,
and provides you with a simple, quick and consistent way of wiring
your view logic to a set of URLs.
"""
router = routers.DefaultRouter()
router.register('find_coach', FindCoachViewSet)
urlpatterns = router.urls