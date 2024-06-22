# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Particular

class Particular_form(UserCreationForm):
    accepted_terms = forms.BooleanField(required=True, label='Acepto los términos y condiciones')
    class Meta:
        model = Particular
        fields = ('usuario', 'nombre', 'apellidos','email', 'telefono', 'nacimiento','pais_residencia')
        
class iniciar_sesion_form(forms.Form):
    usuario = forms.CharField(max_length=31)
    password = forms.CharField(widget=forms.PasswordInput)
