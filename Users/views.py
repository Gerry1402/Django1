from django.shortcuts import render, redirect
from .forms import Particular_form, iniciar_sesion_form
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def principal(request):
    return render(request, '0_principal.html')

def primero(request):
    nombre = 'Gerard'
    d = {'nombre': nombre}
    return render(request, '1_primero.html', d)

def segundo(request):
    return render(request, '2_segundo.html')

def registro(request):
    if request.method == 'POST':
        form = Particular_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, ("Registro completado con éxito"))
            return redirect('principal')
    else:
        form = Particular_form()
    return render(request, 'registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = iniciar_sesion_form(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            password = form.cleaned_data['password']
            print(usuario, password)
            user = authenticate(request, usuario=usuario, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('principal')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = iniciar_sesion_form()
    return render(request, 'login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    # Redirigir a la página de inicio u otra página después de cerrar sesión
    return redirect('principal')