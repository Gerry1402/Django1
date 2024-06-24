from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from phonenumber_field.modelfields import PhoneNumberField
from .utils import lista_paises
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from django.conf import settings

class Usuario(AbstractBaseUser):
    last_login = None
    is_superuser = None
    username = None
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    usuario = models.CharField(max_length=31, unique=True, default='', verbose_name='Usuario')
    email = models.EmailField(default='', max_length=63, unique=True, verbose_name='E-mail')
    telefono = PhoneNumberField(default='', null=False, blank=True, verbose_name='Teléfono')
    pais = models.CharField(max_length=2, choices=lista_paises(), default='ES', verbose_name='País')
    creado_el = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['usuario', 'nombre', 'email', 'telefono', 'pais']
    
    objects = UserManager()

    def __str__(self):
        return self.email

class Particular(Usuario):
    nombre = models.CharField(default='', max_length=31, verbose_name='Nombre')
    apellidos = models.CharField(max_length=31, verbose_name='Apellidos')
    nacimiento = models.DateField(default=(timezone.now()-relativedelta(years=18)).strftime("%Y-%m-%d"), verbose_name='F. Nacimiento')
    cantidad_donada = models.DecimalField(max_digits=31, decimal_places=2, auto_created=True, default=0.00, verbose_name='Donaciones')
    cantidad_recibida = models.DecimalField(max_digits=31, decimal_places=2, auto_created=True, default=0.00, verbose_name='Beneficios')
    anonimo = models.BooleanField(default=False, verbose_name='Anónimo')
    

    REQUIRED_FIELDS = ['nombre', 'apellidos', 'email', 'telefono', 'nacimiento', 'pais_residencia']
    
    class Meta:
        verbose_name = "Particular"
        verbose_name_plural = "Particulares"
   
class Empresa(Usuario):
    nombre = models.CharField(default='', unique=True, max_length=31, verbose_name='Nombre')
    cantidad_donada = models.DecimalField(max_digits=31, decimal_places=2, auto_created=True, default=0.00, verbose_name='Donaciones')
    anonimo = models.BooleanField(default=False, verbose_name='Anónimo')

    REQUIRED_FIELDS = ['nombre', 'email', 'telefono', 'pais_residencia']
    
    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

class ONG(Usuario):
    nombre = models.CharField(default='', unique=True, max_length=31, verbose_name='Nombre')
    donaciones = models.DecimalField(max_digits=31, decimal_places=2, auto_created=True, default=0.00, verbose_name='Donaciones')

    REQUIRED_FIELDS = ['nombre', 'apellidos', 'email', 'telefono', 'nacimiento', 'pais_residencia']
    
    class Meta:
        verbose_name = "ONG"
        verbose_name_plural = "ONGs"