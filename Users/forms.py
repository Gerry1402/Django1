# myapp/forms.py
from django import forms
from .models import Particular

class Part(forms.ModelForm):
    accepted_terms = forms.BooleanField(required=True, label='Acepto los términos y condiciones')
    class Meta:
        model = Particular
        fields = ('usuario','nombre', 'apellidos','email', 'telefono', 'nacimiento','pais_residencia', 'contrasena', 'contrasena_2')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.usuario = self.cleaned_data['usuario']
        user.nombre = self.cleaned_data['nombre']
        user.apellidos = self.cleaned_data['apellidos']
        user.email = self.cleaned_data["email"]
        user.telefono = self.cleaned_data["telefono"]
        user.nacimiento = self.cleaned_data["nacimiento"]
        user.pais_residencia = self.cleaned_data["pais_residencia"]
        user.contrasena = self.cleaned_data["contrasena"]
        user.contrasena_2 = self.cleaned_data["contrasena_2"]
        if commit:
            user.save()
        return user
