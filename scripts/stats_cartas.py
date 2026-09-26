"""Propuesta v3 de ATT / CTL / DEF calibrada con cartas oro de Madfut (ver docs/propuestas/formula-stats.md).

Uso: python3 scripts/stats_cartas.py
Genera data/propuestas/stats-ds.csv y data/propuestas/stats-strikers.csv.
"""
import csv
import re

# Techo de cada stat por posición para cartas base (el mínimo ya no se usa con la escala proporcional).
# Calibrado con las cartas oro top de Madfut: stat principal 86-89 y secundarias bajas.
RANGOS = {
    'PR': {'ATT': (20, 45), 'CTL': (20, 45), 'DEF': (50, 89)},
    'DF': {'ATT': (30, 70), 'CTL': (35, 75), 'DEF': (50, 89)},
    'MC': {'ATT': (45, 86), 'CTL': (50, 89), 'DEF': (35, 80)},
    'DL': {'ATT': (50, 89), 'CTL': (45, 88), 'DEF': (20, 62)},
}


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
    """Escala proporcional: el mejor valor bruto de cada posición va al techo de la posición y el resto en proporción.

    Proporcional (no por percentil): si en el juego un jugador tiene un 10 % más, en la carta también tiene un 10 % más.
    """
    for pos, rangos in RANGOS.items():
        grupo = [r for r in filas if r['posicion'] == pos]
        for s, (_, hi) in rangos.items():
            vmax = max(r['bruto'][s] for r in grupo)
            for r in grupo:
                r[s] = max(1, round(hi * r['bruto'][s] / vmax))


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
        # Key bonus: "+2" a dos stats (ej. "Kick +2/Guard +2").
        for stat, val in re.findall(r'(\w+) \+(\d+)', r['Key bonus']):
            if stat in stats:
                r[stat] += int(val)
        r['posicion'] = pos[r['Position']]
        r['bruto'] = brutas_strikers(r)
        filas.append(r)
    calcular(filas)
    escribir(filas, 'data/propuestas/stats-strikers.csv',
             ['Name (JPN romaji)', 'Name (FR)', 'posicion', 'Element', 'ATT', 'CTL', 'DEF'] + stats)


if __name__ == '__main__':
    ds()
    strikers()
