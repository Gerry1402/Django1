from django.contrib.auth.backends import BaseBackend
from .models import Particular

class ParticularBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Particular.objects.get(usuario=username)
            if user.contrasena == password:  # Aquí deberías utilizar hashing de contraseñas
                return user
        except Particular.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Particular.objects.get(pk=user_id)
        except Particular.DoesNotExist:
            return None