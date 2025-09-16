from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
	path('api/v1/auth/', include('apps.accounts.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
