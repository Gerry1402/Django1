# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Particular, ONG, Empresa

class Part(UserCreationForm):
    accepted_terms = forms.BooleanField(required=True, label='Acepto los términos y condiciones')
    class Meta:
        model = Particular
        fields = ('username', 'nombre','email', 'telefono', 'pais_residencia', 'password1', 'password2')
