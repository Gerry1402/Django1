import pycountry
import gettext
import re


def validate_password_format(contrasena, contrasena_2):
    errores = []
    if contrasena != contrasena_2:
        errores.append('Las contraseñas no coinciden')
    if len(contrasena) < 8:
        errores.append('La contraseña debe tener al menos 8 caracteres.')
    if not re.search(r'[A-Z]', contrasena):
        errores.append('La contraseña debe tener al menos una letra mayúscula.')
    if not re.search(r'[a-z]', contrasena):
        errores.append('La contraseña debe tener al menos una letra minúscula.')
    if not re.search(r'\d', contrasena):
        errores.append('La contraseña debe tener al menos un número.')
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', contrasena):
        errores.append('La contraseña debe tener al menos un carácter especial.')
    if errores != []:
        return errores
    else:
        return True

def lista_paises(idioma_iso='es'):
    """_summary_

    Returns:
        _type_: _description_
    """
    lista_paises = []
    for pais in pycountry.countries:
        trad = gettext.translation('iso3166-1', pycountry.LOCALES_DIR, languages=[idioma_iso])
        trad.install()
        pais_trad = _(pais.name)
        lista_paises.append((pais.alpha_2, pais_trad))
    return sorted(lista_paises, key=lambda x: x[1])