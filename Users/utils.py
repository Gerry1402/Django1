from ipware import get_client_ip
from django.contrib.gis.geoip2 import GeoIP2
import pycountry
import gettext


def get_country_from_ip(request):
    country=None
    ip, is_routable = get_client_ip(request)
    if ip is None:
        return
    g = GeoIP2()
    try:
        country = g.country(ip)['country_name']
    except Exception:
        country = None
    if country:
        country = pycountry.countries.get(name=country).alpha_2
    return

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