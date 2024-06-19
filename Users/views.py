from django.shortcuts import render, redirect
from .forms import Part
from .utils import get_country_from_ip

def principal(request):
    get_country_from_ip(request)
    return render(request, '0_principal.html')

def primero(request):
    nombre = 'Gerard'
    d = {'nombre': nombre}
    return render(request, '1_primero.html', d)

def segundo(request):
    return render(request, '2_segundo.html')

def formulario(request):
    country = get_country_from_ip(request)
    if request.method == 'POST':
        form = Part(request.POST)
        if form.is_valid():
            form.save()
            return redirect('principal')
    else:
        form = Part()
    return render(request, 'signup.html', {'form': form})
