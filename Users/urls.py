from django.urls import path
from Users.views import principal, primero, segundo, registro, iniciar_sesion, cerrar_sesion
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', principal, name='principal'),
    path('primero/', primero, name='primero'),
    path('segundo/', segundo, name='segundo'),
    path('registro/', registro, name="registro"),
    path('iniciar-sesion/', iniciar_sesion, name="iniciar sesion"),
    path('cerrar-sesion/', cerrar_sesion, name="cerrar sesion"),
]