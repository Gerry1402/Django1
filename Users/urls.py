from django.urls import path
from Users.views import principal, primero, segundo, registro, iniciar_sesion, cerrar_sesion
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', principal, name='principal'),
    path('primero/', primero, name='primero'),
    path('segundo/', segundo, name='segundo'),
    path('registro/', registro, name="registro"),
    path('iniciar-sesion/', LoginView.as_view(template_name='login.html'), name="iniciar sesion"),
    path('cerrar-sesion/', LogoutView.as_view(template_name='cerrar_sesion.html'), name="cerrar sesion"),
]