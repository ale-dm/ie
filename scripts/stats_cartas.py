"""Fórmula v4 (aprobada) de ATT / CTL / DEF a partir de la Ultimate Database (IE1-IE3 y GO1-GO3).

Ver docs/formula-stats.md. Uso: python3 scripts/stats_cartas.py
"""
import csv
import re
import statistics

ENTRADA = 'data/fuentes/udb/jugadores-nivel99.csv'
SALIDA = 'data/stats/stats-por-juego.csv'
SALIDA_MEDIA = 'data/stats/stats-media-personaje.csv'
STATS = ['tiro', 'regate', 'tecnica', 'defensa', 'parada', 'velocidad', 'aguante', 'extra']

# (mínimo, jugador mediano, máximo) de cada stat por posición, calibrado con Madfut y con el balance de duelos:
# un delantero gana a un defensa ~68 %, a un portero ~35 %, y un medio atacando gana a un defensa ~50 %.
RANGOS = {
    'PR': {'ATT': (25, 33, 45), 'CTL': (25, 33, 45), 'DEF': (69, 78, 89)},
    'DF': {'ATT': (40, 54, 70), 'CTL': (45, 60, 75), 'DEF': (58, 71, 86)},
    'MC': {'ATT': (58, 72, 86), 'CTL': (62, 76, 89), 'DEF': (45, 62, 80)},
    'DL': {'ATT': (62, 76, 89), 'CTL': (55, 70, 86), 'DEF': (28, 42, 58)},
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
    """Escala lineal por tramos por posición, con todos los juegos juntos.

    El 2 % más flojo va al mínimo, el jugador mediano al valor medio y el 0,5 % mejor al máximo.
    """
    for pos, rangos in RANGOS.items():
        grupo = [r for r in filas if r['posicion'] == pos]
        for s, (lo, mid, hi) in rangos.items():
            vals = [r['bruto'][s] for r in grupo]
            a, m, b = cuantil(vals, SUELO), cuantil(vals, 0.5), cuantil(vals, TECHO)
            for r in grupo:
                x = r['bruto'][s]
                y = mid + (hi - mid) * (x - m) / (b - m) if x >= m else mid + (mid - lo) * (x - m) / (m - a)
                r[s] = round(max(lo, min(hi, y)))


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
