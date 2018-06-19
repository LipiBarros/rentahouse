from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^listar$', listar, name='imovel_listar'),
    url(r'^novo$', adicionar, name='imovel_adicionar'),
    url(r'^alterar/(?P<pk>[0-9]+)$', alterar, name='imovel_alterar'),
    url(r'^excluir/(?P<pk>[0-9]+)$', excluir, name='imovel_excluir'),
]
