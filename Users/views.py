from django.shortcuts import render, redirect
from .forms import Part
from django.contrib.auth import authenticate, login
from .decorators import login_required

@login_required
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
        form = Part(request.POST)
        form
        if form.is_valid():
            form.save()
            return redirect('principal')
    else:
        form = Part()
    return render(request, 'registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['user_id'] = user.id
            return redirect('principal')  # Redirige a la página de inicio o a donde prefieras
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'login.html')
