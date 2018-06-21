from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
import rentahouse.core.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', rentahouse.core.views.listar),
    re_path(r'^imovel/', include('rentahouse.core.urls')),
    re_path(r'^', include('rentahouse.usuario.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
