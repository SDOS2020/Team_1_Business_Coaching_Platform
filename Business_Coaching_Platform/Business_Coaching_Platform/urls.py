from django.contrib import admin
from django.urls import include, path
from user import views as user_views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns = [
    path('', include('home.urls')),
    path('', include('user.urls')),
    path('', include('dashboard.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
