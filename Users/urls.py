from django.urls import path
from Users.views import principal, primero, segundo, formulario

urlpatterns = [
    path('', principal, name='principal'),
    path('primero/', primero, name='primero'),
    path('segundo/', segundo, name='segundo'),
    path('formulario/', formulario, name="formulario")
]