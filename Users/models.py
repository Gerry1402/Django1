from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractBaseUser
from datetime import date
from .utils import get_country_from_ip, lista_paises

class BaseUser(AbstractBaseUser):
    username = models.CharField(max_length=31, unique=True, verbose_name='Nombre')
    email = models.EmailField(unique=True, verbose_name='E-mail')
    telefono = PhoneNumberField(null=False, blank=False, unique=True, verbose_name='Teléfono')
    pais_residencia = models.CharField(max_length=7, choices=lista_paises(), default='ES', verbose_name='País')
    creado_el = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    ultimo_login = models.DateTimeField(auto_now=True, verbose_name='Último inicio de sesión')
    def __str__(self):
        return self.username

class Particular(BaseUser):
    nombre = models.CharField(max_length=31, unique=True, verbose_name='Nombre')
    anonimo = models.BooleanField(default=False, verbose_name='Anonimato')
    nacimiento = models.DateField(null=False, blank=False, verbose_name='Fecha nacimiento')
    cantidad_donada = 0
    def menor(self):
        """Verifica si el usuario es menor de edad."""
        today = date.today()
        age = today.year - self.nacimiento.year - ((today.month, today.day) < (self.nacimiento.month, self.nacimiento.day))
        return age < 18

class ONG(BaseUser):
    SECTORES = [
        ('Educación', 'Educación'),
        ('Salud', 'Salud'),
        ('Alimentación', 'Alimentación'),
        ('Arte y Cultura', 'Arte y Cultura'),
        ('Ciencia y Tecnología', 'Ciencia y Tecnología'),
        ('Vivienda', 'Vivienda'),
        ('Otro', 'Otro'),
    ]

class Empresa(BaseUser):
    SECTORES = [
        ('Educación', 'Educación'),
        ('Salud', 'Salud'),
        ('Alimentación', 'Alimentación'),
        ('Arte y Cultura', 'Arte y Cultura'),
        ('Ciencia y Tecnología', 'Ciencia y Tecnología'),
        ('Vivienda', 'Vivienda'),
        ('Otro', 'Otro'),
    ]