from django.contrib import admin
from django.urls import path, include, re_path
import rentahouse.core.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', rentahouse.core.views.home),
    re_path(r'^imovel/', include('rentahouse.core.urls')),
]
