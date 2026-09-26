"""Propuesta v4 de ATT / CTL / DEF a partir de la Ultimate Database (IE1-IE3 y GO1-GO3).

Ver docs/propuestas/formula-stats.md. Uso: python3 scripts/stats_cartas.py
"""
import csv
import re
import statistics

ENTRADA = 'data/fuentes/udb/jugadores-nivel99.csv'
SALIDA = 'data/propuestas/stats-cartas.csv'
SALIDA_MEDIA = 'data/propuestas/stats-media-personaje.csv'
STATS = ['tiro', 'regate', 'tecnica', 'defensa', 'parada', 'velocidad', 'aguante', 'extra']

# Rango de cada stat por posición, de la carta base más floja a la oro top (calibrado con Madfut).
RANGOS = {
    'PR': {'ATT': (25, 45), 'CTL': (25, 45), 'DEF': (60, 89)},
    'DF': {'ATT': (40, 70), 'CTL': (45, 75), 'DEF': (60, 89)},
    'MC': {'ATT': (55, 86), 'CTL': (60, 89), 'DEF': (40, 80)},
    'DL': {'ATT': (60, 89), 'CTL': (55, 88), 'DEF': (30, 62)},
}
SUELO, TECHO = 0.02, 0.995  # percentiles que marcan el mínimo y el techo de cada rango


def cuantil(valores, p):
    valores = sorted(valores)
    return valores[min(len(valores) - 1, int(p * len(valores)))]


def normalizar(filas):
    """Cada stat se pasa a unidades z dentro de su juego, para que IE (~30-100) y GO (~30-200) sean equivalentes."""
    for juego in {r['juego'] for r in filas}:
        grupo = [r for r in filas if r['juego'] == juego]
        for s in STATS:
            media = statistics.mean(r[s] for r in grupo)
            desv = statistics.pstdev(r[s] for r in grupo)
            for r in grupo:
                r['z_' + s] = (r[s] - media) / desv


def brutas(r):
    z = lambda s: r['z_' + s]
    att = .8 * z('tiro') + .2 * z('tecnica')
    ctl = .5 * z('regate') + .25 * z('tecnica') + .25 * z('velocidad')
    if r['posicion'] == 'PR':
        de = .8 * z('parada') + .2 * z('defensa')
    else:
        de = .8 * z('defensa') + .1 * z('tecnica') + .1 * z('aguante')
    return {'ATT': att, 'CTL': ctl, 'DEF': de}


def escalar(filas):
    """Escala lineal por posición, con todos los juegos juntos."""
    for pos, rangos in RANGOS.items():
        grupo = [r for r in filas if r['posicion'] == pos]
        for s, (lo, hi) in rangos.items():
            vals = [r['bruto'][s] for r in grupo]
            a, b = cuantil(vals, SUELO), cuantil(vals, TECHO)
            for r in grupo:
                r[s] = round(max(lo, min(hi, lo + (hi - lo) * (r['bruto'][s] - a) / (b - a))))


def media_por_personaje(filas):
    """Media de las versiones base (sin paréntesis: ni adulto, ni Mixi-Max…) de cada personaje en todos los juegos."""
    grupos = {}
    for r in filas:
        if '(' in r['nombre']:
            continue
        clave = (re.sub(r'\s+', ' ', r['nombre']).strip(), r['posicion'])
        grupos.setdefault(clave, []).append(r)
    salida = []
    for (nombre, pos), rs in sorted(grupos.items()):
        salida.append({'nombre': nombre, 'posicion': pos, 'juegos': ' '.join(sorted({r['juego'] for r in rs})),
                       **{s: round(statistics.mean(r[s] for r in rs)) for s in ['ATT', 'CTL', 'DEF']}})
    return salida


def main():
    filas = list(csv.DictReader(open(ENTRADA)))
    for r in filas:
        for s in STATS:
            r[s] = float(r[s])
    normalizar(filas)
    for r in filas:
        r['bruto'] = brutas(r)
    escalar(filas)
    with open(SALIDA, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['juego', 'nombre', 'posicion', 'elemento', 'ATT', 'CTL', 'DEF'], extrasaction='ignore')
        w.writeheader()
        w.writerows(filas)
    with open(SALIDA_MEDIA, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['nombre', 'posicion', 'juegos', 'ATT', 'CTL', 'DEF'])
        w.writeheader()
        w.writerows(media_por_personaje(filas))


if __name__ == '__main__':
    main()
