from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('movies/', include('movies.urls')),
    path('series/', include('series.urls')),
    path('actors/', include('actors.urls')),
    path('celebrities/', include('celebrities.urls')),
    path('__reload__/', include('django_browser_reload.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)