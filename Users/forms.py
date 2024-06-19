# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Particular

class Part(UserCreationForm):
    accepted_terms = forms.BooleanField(required=True, label='Acepto los términos y condiciones')
    class Meta:
        model = Particular
        fields = ('USERNAME_FIELD', 'nombre', 'apellidos','email', 'telefono', 'nacimiento','pais_residencia', 'password1', 'password2')
