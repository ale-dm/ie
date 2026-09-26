"""Criba las fichas de data/stats/stats-por-juego.csv y deja solo las que serán cartas.

Reglas (GDD 2.2):
- Orden de prioridad: IE1 > IE2 > IE3 > GO1 > GO2 > GO3. Si un jugador se repite, se queda su primera ficha.
- Excepción: la línea del Raimon (data/config/linea-raimon.csv) tiene una versión por juego. En ese archivo el nombre
  es el completo de la ficha (con paréntesis si los tiene) y la posición, opcional, elige entre fichas repetidas.
- Los jugadores de la saga original que reaparecen en GO se descartan, salvo sus versiones adultas.
- Los personajes nuevos de GO conservan sus versiones especiales (Mixi-Max, etc.), una vez cada una.

Uso: python3 scripts/cribar_cartas.py
"""
import csv
import re
import unicodedata

ENTRADA = 'data/stats/stats-por-juego.csv'
LINEA_RAIMON = 'data/config/linea-raimon.csv'
SALIDA = 'data/cartas/cartas.csv'
ORDEN_JUEGOS = ['IE1', 'IE2', 'IE3', 'GO1', 'GO2', 'GO3']
ADULTO = re.compile(r'\badult[oae]?\b', re.I)


def clave(nombre):
    """Nombre base comparable entre juegos: sin tildes, sin paréntesis, sin "adulto", sin guiones."""
    s = unicodedata.normalize('NFKD', nombre).encode('ascii', 'ignore').decode().lower()
    s = re.sub(r'\(.*?\)', ' ', s)
    s = ADULTO.sub(' ', s)
    s = re.sub(r'[-._"]', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def completo(nombre):
    """Nombre completo comparable (incluye lo que va entre paréntesis)."""
    s = unicodedata.normalize('NFKD', nombre).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'\s+', ' ', re.sub(r'[-._"()]', ' ', s)).strip()


def variante(nombre):
    """Texto de la versión especial (lo que va entre paréntesis), o '' si es la versión base."""
    if ADULTO.search(nombre):
        return 'Adulto'
    m = re.search(r'\((.*?)\)', nombre)
    return m.group(1).strip() if m else ''


def main():
    filas = list(csv.DictReader(open(ENTRADA)))
    filas.sort(key=lambda r: (ORDEN_JUEGOS.index(r['juego']), int(r['orden'])))
    linea = {(r['juego'], completo(r['nombre'])): (r['version'], r['posicion']) for r in csv.DictReader(open(LINEA_RAIMON))}

    originales = set()   # personajes que salen en IE1-IE3
    vistos = set()       # claves de personaje ya usadas (versión base)
    versiones = set()    # (juego, clave) de la línea del Raimon ya usadas
    especiales = set()   # (clave, variante) de versiones especiales ya usadas
    cartas = []
    for r in filas:
        k, var, juego = clave(r['nombre']), variante(r['nombre']), r['juego']
        en_linea = linea.get((juego, completo(r['nombre'])))
        if en_linea and en_linea[1] and en_linea[1] != r['posicion']:
            en_linea = None  # ficha repetida del mismo personaje en otra posición
        saga_go = juego.startswith('GO')
        if not saga_go:
            originales.add(k)
        version = None
        if en_linea:
            if (juego, k) not in versiones:
                versiones.add((juego, k))
                vistos.add(k)
                version = en_linea[0]
        elif saga_go and k in originales:
            if var == 'Adulto' and (k, var) not in especiales:
                especiales.add((k, var))
                version = 'Adulto'
        elif var:
            if (k, var) not in especiales:
                especiales.add((k, var))
                version = var
        elif k not in vistos:
            vistos.add(k)
            version = juego
        if version:
            cartas.append({'juego': juego, 'version': version, 'nombre': re.sub(r'\s+', ' ', r['nombre']).strip(), 'posicion': r['posicion'],
                           'elemento': r['elemento'], 'ATT': r['ATT'], 'CTL': r['CTL'], 'DEF': r['DEF'],
                           'tecnicas': r['tecnicas']})
    with open(SALIDA, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(cartas[0].keys()))
        w.writeheader()
        w.writerows(cartas)
    print(len(filas), 'fichas ->', len(cartas), 'cartas')


if __name__ == '__main__':
    main()
