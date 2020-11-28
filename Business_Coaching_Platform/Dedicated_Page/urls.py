from django.urls import path, include
from .views import PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', PostViewSet, basename='post')

urlpatterns = [
    path('viewset/', include(router.urls))
]