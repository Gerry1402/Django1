# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Particular
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from phonenumber_field.formfields import RegionalPhoneNumberWidget

class Particular_form(UserCreationForm):
    accepted_terms = forms.BooleanField(required=True, label='Acepto los términos y condiciones')
    class Meta:
        model = Particular
        fields = ('usuario', 'nombre', 'apellidos','email', 'telefono', 'nacimiento','pais')
        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'simple-field', 'placeholder': 'SocialNexus'}),
            'nombre': forms.TextInput(attrs={'class': 'simple-field', 'placeholder': 'Social'}),
            'apellidos': forms.TextInput(attrs={'class': 'simple-field', 'placeholder': 'Nexus'}),
            'telefono': RegionalPhoneNumberWidget(attrs={'class': 'simple-field', 'placeholder': '+34 999 999 999'}),
            'nacimiento': forms.DateInput(attrs={'class': 'simple-field', 'type': 'date', 'max':(timezone.now()-relativedelta(years=18)).strftime("%Y-%m-%d"), 'min':(timezone.now()-relativedelta(years=120)).strftime("%Y-%m-%d")}),
            'email': forms.EmailInput(attrs={'class': 'simple-field', 'placeholder': 'correo@socialnexus.com'}),
            'pais': forms.Select(attrs={'class': 'simple-field'}),
            'password1': forms.PasswordInput(attrs={'class': 'simple-field'}),
            'password2': forms.PasswordInput(attrs={'class': 'simple-field'}),
            'accepted_terms': forms.CheckboxInput(attrs={'class': 'last-field'}),
        }
        
class iniciar_sesion_form(forms.Form):
    usuario = forms.CharField(max_length=31)
    password = forms.CharField(widget=forms.PasswordInput)
