# decorators.py
from django.shortcuts import redirect

def login_required(function):
    def wrap(request, *args, **kwargs):
        if 'user_id' not in request.session:
            return redirect('iniciar sesion')
        return function(request, *args, **kwargs)
    return wrap