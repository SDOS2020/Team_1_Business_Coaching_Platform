from django.urls import path, include
from django.conf.urls import url
from .views import PostViewSet
from rest_framework.routers import DefaultRouter

import dedicated_page.views as dedicated_page_views
from django.views.generic import TemplateView


router = DefaultRouter()
router.register('post', PostViewSet, basename='post')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/<int:pk>/', include(router.urls)),
    url(r'^dedicated_page/(?P<pk>\d+)/$', dedicated_page_views.dedicated_page, name='dedicated_page'),
    path('create_post/', PostViewSet.as_view({"post": "create_post"}), name='new_post'),
]