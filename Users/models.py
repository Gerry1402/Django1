from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from .utils import lista_paises
from django.utils import timezone
from dateutil.relativedelta import relativedelta

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    country_code = models.CharField(max_length=5, blank=True, null=True)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "password"]
    objects = CustomUserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class Particular(AbstractUser):
    
    usuario = models.CharField(max_length=31, unique=True, default='', verbose_name='Usuario')
    nombre = models.CharField(max_length=31, verbose_name='Nombre')
    apellidos = models.CharField(max_length=31, verbose_name='Apellidos')
    email = models.EmailField(default='default@example.com', max_length=63, unique=True, verbose_name='E-mail')
    telefono = PhoneNumberField(null=False, blank=True, unique=True, verbose_name='Teléfono')
    nacimiento = models.DateField(default= timezone.now()-relativedelta(years=18), verbose_name='Fecha nacimiento')
    pais_residencia = models.CharField(max_length=7, choices=lista_paises(), default='ES', verbose_name='País')
    creado_el = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    anonimo = models.BooleanField(default=False, verbose_name='Anonimato')
    cantidad_donada = models.DecimalField(max_digits=31, decimal_places=2, auto_created=True, default=0.00, verbose_name='Donaciones')

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['nombre', 'apellidos', 'email', 'telefono', 'nacimiento', 'pais_residencia']

    def __str__(self):
        return self.email
   

# class ONG(AbstractBaseUser):
#     usario = models.CharField(max_length=31, unique=True, verbose_name='Nombre Usuario')
#     email = models.EmailField(default='default@example.com', max_length=63,unique=True, verbose_name='E-mail')
#     telefono = PhoneNumberField(unique=True, verbose_name='Teléfono')
#     pais_residencia = models.CharField(max_length=7, choices=lista_paises(), default='ES', verbose_name='País')
#     creado_el = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
#     ultima_modificación = models.DateTimeField(auto_now=True, verbose_name='Última modificación')
#     cantidad_donada = models.DecimalField(max_digits=31, decimal_places=2, auto_created=True, default=0.00, verbose_name='Donaciones')
#     USERNAME_FIELD = usario

# class Empresa(AbstractBaseUser):
#     usario = models.CharField(max_length=31, unique=True, verbose_name='Nombre Usuario')
#     email = models.EmailField(default='default@example.com', max_length=63, unique=True, verbose_name='E-mail')
#     telefono = PhoneNumberField(unique=True, verbose_name='Teléfono')
#     pais_residencia = models.CharField(max_length=7, choices=lista_paises(), default='ES', verbose_name='País')
#     creado_el = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
#     ultima_modificación = models.DateTimeField(auto_now=True, verbose_name='Última modificación')
#     anonimo = models.BooleanField(default=False, verbose_name='Anonimato')
#     cantidad_donada = models.DecimalField(max_digits=31, decimal_places=2, auto_created=True, default=0.00, verbose_name='Donaciones')