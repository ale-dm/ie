"""Propuesta de cálculo de ATT / CTL / DEF a partir de las stats de DS/3DS (ver docs/propuestas/formula-stats.md)."""
import bisect
import csv

ENTRADA = 'data/fuentes/ds/ie1-ie2-ie3-nivel99.csv'
SALIDA = 'data/propuestas/stats-ds.csv'
STATS = ['Kick', 'Body', 'Control', 'Guard', 'Speed', 'Stamina', 'Guts']

# Factor por posición sobre (ATT, CTL, DEF): la stat principal no se reduce, las secundarias sí.
ROL = {'PR': (0.55, 0.8, 1.0), 'DF': (0.8, 0.9, 1.0), 'MC': (0.9, 1.0, 0.85), 'DL': (1.0, 0.9, 0.6)}


def brutas(r):
    att = .8 * r['Kick'] + .1 * r['Control'] + .1 * r['Guts']
    ctl = .5 * r['Body'] + .25 * r['Control'] + .25 * r['Speed']
    if r['posicion'] == 'PR':
        de = .8 * r['Guard'] + .1 * r['Body'] + .1 * r['Guts']
    else:
        de = .7 * r['Guard'] + .1 * r['Control'] + .1 * r['Stamina'] + .1 * r['Guts']
    return att, ctl, de


def main():
    filas = list(csv.DictReader(open(ENTRADA)))
    for r in filas:
        for s in STATS:
            r[s] = int(r[s])
        r['bruto'] = brutas(r)
    orden = [sorted(r['bruto'][i] for r in filas) for i in range(3)]
    for r in filas:
        for i, s in enumerate(['ATT', 'CTL', 'DEF']):
            p = bisect.bisect_right(orden[i], r['bruto'][i]) / len(filas)
            r[s] = max(1, min(99, round((50 + 49 * p ** 1.3) * ROL[r['posicion']][i])))
    campos = ['juego', 'equipo', 'nombre', 'posicion', 'elemento', 'ATT', 'CTL', 'DEF'] + STATS
    with open(SALIDA, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=campos, extrasaction='ignore')
        w.writeheader()
        w.writerows(filas)


if __name__ == '__main__':
    main()
