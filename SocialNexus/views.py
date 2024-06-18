from django.http import HttpResponse # type: ignore
from django.shortcuts import render # type: ignore

def saludo(request):
    nombre = 'Gerard'
    d = {'nombre': nombre}
    return render(request, 'secundario.html', d)