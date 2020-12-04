from django.urls import path, include
from django.conf.urls import url
from .views import PostViewSet
from rest_framework.routers import DefaultRouter

import dedicated_page.views as dedicated_page_views
from django.views.generic import TemplateView

router = DefaultRouter()
router.register('post', PostViewSet, basename='post')

urlpatterns = [
    # path('viewset/', include(router.urls))
    path('api/', include(router.urls)),
    path('api/<int:pk>/', include(router.urls)),
    # path('post/',TemplateView.as_view(template_name='page.html')),
    # path('post/new/<int:pk>',dedicated_page_views.create_post, name='post_create'),
    url(r'^dedicated_page/(?P<pk>\d+)/$', dedicated_page_views.dedicated_page, name='dedicated_page'),

]