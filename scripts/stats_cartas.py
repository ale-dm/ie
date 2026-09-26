"""Propuesta v2 de ATT / CTL / DEF calibrada con cartas oro de Madfut (ver docs/propuestas/formula-stats.md).

Uso: python3 scripts/stats_cartas.py
Genera data/propuestas/stats-ds.csv y data/propuestas/stats-strikers.csv.
"""
import bisect
import csv

# Rango de cada stat por posición para cartas base (de la peor verde a la mejor naranja).
# Techo calibrado con las cartas oro top de Madfut: stat principal 86-89 y secundarias bajas.
RANGOS = {
    'PR': {'ATT': (20, 45), 'CTL': (20, 45), 'DEF': (50, 89)},
    'DF': {'ATT': (30, 70), 'CTL': (35, 75), 'DEF': (50, 89)},
    'MC': {'ATT': (45, 86), 'CTL': (50, 89), 'DEF': (35, 80)},
    'DL': {'ATT': (50, 89), 'CTL': (45, 88), 'DEF': (20, 62)},
}
CURVA = 1.3  # >1 reserva los valores altos para los mejores de cada posición


def brutas_ds(r):
    att = .8 * r['Kick'] + .1 * r['Control'] + .1 * r['Guts']
    ctl = .5 * r['Body'] + .25 * r['Control'] + .25 * r['Speed']
    if r['posicion'] == 'PR':
        de = .8 * r['Guard'] + .1 * r['Body'] + .1 * r['Guts']
    else:
        de = .7 * r['Guard'] + .1 * r['Control'] + .1 * r['Stamina'] + .1 * r['Guts']
    return {'ATT': att, 'CTL': ctl, 'DEF': de}


def brutas_strikers(r):
    att = .8 * r['Kick'] + .2 * r['Control']
    ctl = .5 * r['Body'] + .25 * r['Control'] + .25 * r['Speed']
    de = (.8 * r['Catch'] + .2 * r['Guard']) if r['posicion'] == 'PR' else r['Guard']
    return {'ATT': att, 'CTL': ctl, 'DEF': de}


def calcular(filas):
    """Percentil de cada stat bruta dentro de su posición, llevado al rango de la posición."""
    for pos, rangos in RANGOS.items():
        grupo = [r for r in filas if r['posicion'] == pos]
        for s, (lo, hi) in rangos.items():
            orden = sorted(r['bruto'][s] for r in grupo)
            for r in grupo:
                p = bisect.bisect_right(orden, r['bruto'][s]) / len(orden)
                r[s] = round(lo + (hi - lo) * p ** CURVA)


def escribir(filas, salida, campos):
    with open(salida, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=campos, extrasaction='ignore')
        w.writeheader()
        w.writerows(filas)


def ds():
    stats = ['Kick', 'Body', 'Control', 'Guard', 'Speed', 'Stamina', 'Guts']
    filas = list(csv.DictReader(open('data/fuentes/ds/ie1-ie2-ie3-nivel99.csv')))
    for r in filas:
        for s in stats:
            r[s] = int(r[s])
        r['bruto'] = brutas_ds(r)
    calcular(filas)
    escribir(filas, 'data/propuestas/stats-ds.csv',
             ['juego', 'equipo', 'nombre', 'posicion', 'elemento', 'ATT', 'CTL', 'DEF'] + stats)


def strikers():
    stats = ['Kick', 'Body', 'Control', 'Guard', 'Speed', 'Catch']
    pos = {'GK': 'PR', 'DF': 'DF', 'MF': 'MC', 'FW': 'DL'}
    filas = []
    for r in csv.DictReader(open('data/fuentes/strikers/players.csv')):
        # Fuera: managers (stats a 0) y versiones "Trainer/Coach" y "Armed" con todo a 90 (no son jugadores reales).
        if not r['Kick'] or float(r['Kick']) == 0 or '(Trainer)' in r['Name (JPN romaji)'] or 'Arme' in r['Name (JPN romaji)']:
            continue
        for s in stats:
            r[s] = float(r[s])
        r['posicion'] = pos[r['Position']]
        r['bruto'] = brutas_strikers(r)
        filas.append(r)
    calcular(filas)
    escribir(filas, 'data/propuestas/stats-strikers.csv',
             ['Name (JPN romaji)', 'Name (FR)', 'posicion', 'Element', 'ATT', 'CTL', 'DEF'] + stats)


if __name__ == '__main__':
    ds()
    strikers()
