
import pycountry
import gettext

lista_regiones = []
for region in pycountry.subdivisions.get(country_code='ES'):
    trad = gettext.translation('iso3166-2', pycountry.LOCALES_DIR, languages=['es'])
    trad.install()
    region_trad = _(region.name)
    element = (region.code, region_trad, region.type)
    lista_regiones.append(element)
    print(element)
lista_regiones = sorted(lista_regiones, key=lambda x: x[1])