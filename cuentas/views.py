from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms
from .forms import UsuarioForm, PerfilForm

@login_required
def editar_perfil(request):
    perfil = request.user.perfil

    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil)

        if usuario_form.is_valid() and perfil_form.is_valid():
            usuario_form.save()
            perfil_form.save()
            return redirect('ver_perfil')
    else:
        usuario_form = UsuarioForm(instance=request.user)
        perfil_form = PerfilForm(instance=perfil)

    return render(
        request,
        'cuentas/editar_perfil.html',
        {
            'usuario_form': usuario_form,
            'perfil_form': perfil_form
        }
    )


@login_required
def ver_perfil(request):
    perfil = request.user.perfil
    return render(request, 'cuentas/perfil.html', {'perfil': perfil})


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('inicio')
    else:
        form = AuthenticationForm()

    return render(request, 'cuentas/login.html', {'form': form})


@login_required
def logout_usuario(request):
    logout(request)
    return redirect('inicio')


def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, 'Usuario creado correctamente')
            return redirect('inicio')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'cuentas/registro.html', {'form': form})


# Create your views here.
