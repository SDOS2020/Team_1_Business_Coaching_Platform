from django.urls import path,include
from rest_framework import routers
from .views import FindCoachViewSet,find_coach

"""
REST framework adds support for automatic URL routing to Django,
and provides you with a simple, quick and consistent way of wiring
your view logic to a set of URLs.
"""
router = routers.DefaultRouter()
router.register('find_coach', FindCoachViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('api/', include(router.urls)),
    path('find_coach/', find_coach, name='find_coach'),
]