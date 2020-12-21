from django.urls import path, include
import dashboard.views as dashboard_views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('chat', dashboard_views.ChatViewSet, basename='chat')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/<int:pk>/', include(router.urls)),
    path('dashboard/', dashboard_views.dashboard, name='dashboard'),
]