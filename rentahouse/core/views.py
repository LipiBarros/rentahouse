from django.shortcuts import render, redirect
from .forms import ImovelForm


def home(request):
    return render(request, 'index.html')


def adicionar(request, template_name='imovel_form.html'):
    imovel = ImovelForm(request.POST or None)
    if imovel.is_valid():
        imovel.save()
        return redirect('/')

    return render(request, template_name, {'titulo': 'Novo', 'form': imovel})
