from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^entrar$', entrar, name='usuario_entrar'),
    url(r'^sair$', sair, name='usuario_sair'),
]
