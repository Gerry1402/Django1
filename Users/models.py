from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser
from .utils import get_country_from_ip, lista_paises
from django.utils import timezone
from dateutil.relativedelta import relativedelta

class Particular(AbstractBaseUser):
    USERNAME_FIELD = models.CharField(max_length=31, unique=True, verbose_name='Nombre Usuario')
    nombre = models.CharField(max_length=31, verbose_name='Nombre')
    apellidos = models.CharField(max_length=31, verbose_name='Apellidos')
    email = models.EmailField(default='default@example.com', max_length=63, unique=True, verbose_name='E-mail')
    telefono = PhoneNumberField(null=False, blank=False, unique=True, verbose_name='Teléfono')
    nacimiento = models.DateField(default= timezone.now()-relativedelta(years=18), verbose_name='Fecha nacimiento')
    pais_residencia = models.CharField(max_length=7, choices=lista_paises(), default='ES', verbose_name='País')
    creado_el = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    ultima_modificación = models.DateTimeField(auto_now=True, verbose_name='Última modificación')
    anonimo = models.BooleanField(default=False, verbose_name='Anonimato')
    cantidad_donada = models.DecimalField(max_digits=31, decimal_places=2, auto_created=True, default=0.00, verbose_name='Donaciones')

class ONG(AbstractBaseUser):
    USERNAME_FIELD = models.CharField(max_length=31, unique=True, verbose_name='Nombre Usuario')
    email = models.EmailField(default='default@example.com', max_length=63,unique=True, verbose_name='E-mail')
    telefono = PhoneNumberField(unique=True, verbose_name='Teléfono')
    pais_residencia = models.CharField(max_length=7, choices=lista_paises(), default='ES', verbose_name='País')
    creado_el = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    ultima_modificación = models.DateTimeField(auto_now=True, verbose_name='Última modificación')
    anonimo = models.BooleanField(default=False, verbose_name='Anonimato')
    cantidad_donada = models.DecimalField(max_digits=31, decimal_places=2, auto_created=True, default=0.00, verbose_name='Donaciones')

class Empresa(AbstractBaseUser):
    USERNAME_FIELD = models.CharField(max_length=31, unique=True, verbose_name='Nombre Usuario')
    email = models.EmailField(default='default@example.com', max_length=63, unique=True, verbose_name='E-mail')
    telefono = PhoneNumberField(unique=True, verbose_name='Teléfono')
    pais_residencia = models.CharField(max_length=7, choices=lista_paises(), default='ES', verbose_name='País')
    creado_el = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    ultima_modificación = models.DateTimeField(auto_now=True, verbose_name='Última modificación')
    anonimo = models.BooleanField(default=False, verbose_name='Anonimato')
    cantidad_donada = models.DecimalField(max_digits=31, decimal_places=2, auto_created=True, default=0.00, verbose_name='Donaciones')