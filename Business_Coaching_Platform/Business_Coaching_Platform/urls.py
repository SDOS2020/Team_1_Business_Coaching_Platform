from django.contrib import admin
from django.urls import include, path
from user import views as user_views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf import settings
from enrolment.templates import enrolment

urlpatterns = [
    path('', include('home.urls')),
    path('', include('user.urls')),
    path('', include('enrolment.urls')),
    path('', include('dashboard.urls')),
    path('notification/', include('notification.urls')),
    path('admin/', admin.site.urls),
    path('find_coach/', TemplateView.as_view(template_name='enrolment/find_coach.html')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
