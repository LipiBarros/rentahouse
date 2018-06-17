from django.conf.urls import url
from .views import *


urlpatterns = [
    # url(r'^$', listar, name='meta_listar'),
    url(r'^novo$', adicionar, name='imovel_adicionar'),
    # url(r'^alterar/(?P<pk>[0-9]+)$', alterar, name='meta_alterar'),
    # url(r'^excluir/(?P<pk>[0-9]+)$', excluir, name='meta_excluir'),
]
