from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


def entrar(request, template_name='entrar.html'):
    next = request.GET.get('next', '/')
    if request.method == "POST":
        nome_usuario = request.POST['nome_usuario']
        senha = request.POST['senha']
        usuario = authenticate(username=nome_usuario, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect(next)
        else:
            messages.error(request, 'Usuário ou senha incorreto.')
            return redirect(settings.LOGIN_URL)

    return render(request, template_name, {'redirect_to': next})


def sair(request):
    logout(request)
    return HttpResponseRedirect('/')
