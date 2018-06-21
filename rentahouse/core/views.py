from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ImovelForm, Imovel
from django.db.models import Q


def paginador(request, qt_por_pagina, lista):
    resultados_por_pagina = request.GET.get("resultados_por_pagina")

    if not resultados_por_pagina or not resultados_por_pagina.isdigit():
        resultados_por_pagina = qt_por_pagina

    paginador = Paginator(lista, resultados_por_pagina)

    pagina = request.GET.get('pagina')

    try:
        pagina_atual = paginador.page(pagina)
    except PageNotAnInteger:
        pagina = 1
        pagina_atual = paginador.page(pagina)
    except EmptyPage:
        pagina = paginador.num_pages
        pagina_atual = paginador.page(pagina)

    lista_paginas = []
    for i in range(paginador.num_pages):
        lista_paginas.append(i + 1)

    paginacao = [
        pagina_atual,
        pagina,
        lista_paginas
    ]
    return paginacao


def listar(request, template_name='imovel_listar.html'):
    pesquisa = request.GET.get("pesquisa")
    if pesquisa:
        imoveis = Imovel.objects.filter(
            Q(titulo__icontains=pesquisa) |
            Q(descricao__icontains=pesquisa)
        )
    else:
        pesquisa = ''
        imoveis = Imovel.objects.all().order_by('-id')

    paginacao = paginador(request, 10, imoveis)

    template_data = {
        'lista': imoveis,
        'pesquisa': pesquisa,
        'pagina_atual': paginacao[0],
        'pagina': paginacao[1],
        'lista_paginas': paginacao[2],
    }

    return render(request, template_name, template_data)


@login_required
def adicionar(request, template_name='imovel_form.html'):
    imovel = ImovelForm(request.POST, request.FILES)
    if imovel.is_valid():
        imovel.save()
        return redirect('imovel_listar')
    else:
        imovel = ImovelForm()
    return render(request, template_name, {'titulo': 'Novo', 'form': imovel})


@login_required
def excluir(request, pk, template_name='imovel_excluir.html'):
    imovel = Imovel.objects.get(pk=pk)
    if request.method == 'POST':
        imovel.delete()
        return redirect('imovel_listar')

    return render(request, template_name, {'titulo': 'Excluir', 'imovel': imovel})


@login_required
def alterar(request, pk, template_name='imovel_form.html'):
    imovel = get_object_or_404(Imovel, pk=pk)
    if request.method == "POST":
        imovelForm = ImovelForm(request.POST, request.FILES, instance=imovel)
        if imovelForm.is_valid():
            imovelForm.save()
            return redirect('imovel_listar')
    else:
        imovelForm = ImovelForm(instance=imovel)
    return render(request, template_name, {'titulo': 'Alterar', 'form': imovelForm})
