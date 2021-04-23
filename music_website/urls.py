from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/',include('music.urls')),
    path('',RedirectView.as_view(url='music/', permanent=False))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)