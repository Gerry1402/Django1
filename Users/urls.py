from django.urls import path
from Users.views import principal, primero, segundo, registro, iniciar_sesion

urlpatterns = [
    path('', principal, name='principal'),
    path('primero/', primero, name='primero'),
    path('segundo/', segundo, name='segundo'),
    path('registro/', registro, name="registro"),
    path('iniciar-sesion/', iniciar_sesion, name="iniciar sesion"),
]