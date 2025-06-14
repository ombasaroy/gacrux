from django.contrib import admin

from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.static import serve

from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gacrux_app.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'gacrux_app.views.custom_404_view'
