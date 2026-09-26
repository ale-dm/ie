"""Genera docs/ejemplos-cartas.md a partir de data/stats/stats-por-juego.csv. Uso: python3 scripts/ejemplos_cartas.py"""
import collections
import csv
import random

JUEGOS = ['IE1', 'IE2', 'IE3', 'GO1', 'GO2', 'GO3']
ELEMENTOS = {'fuego': 'Fuego', 'aire': 'Aire', 'bosque': 'Bosque', 'tierra': 'Tierra', '': '—'}
GRUPOS = [
    ('Raimon (IE1)', ['Mark Evans', 'Nathan Swift', 'Jack Wallside', 'Jim Wraith', 'Tod Ironside', 'Bobby Shearer',
                      'Steve Grim', 'Tim Saunders', 'Sam Kincaid', 'Jude Sharp', 'Erik Eagle', 'Maxwell Carson',
                      'Kevin Dragonfly', 'William Glass', 'Axel Blaze']),
    ('Rivales IE1–IE2', ['Joseph King', 'David Samford', 'Byron Love', 'Xene', 'Janus', 'Torch', 'Gazelle']),
    ('Inazuma Japón y mundial (IE3)', ['Darren LaChance', 'Hector Helio', 'Hurley Kane', 'Shawn Froste', 'Caleb Stonewall',
                                       'Jordan Greenway', 'Xavier Foster', 'Paolo Bianchi', 'Edgar Partinus',
                                       'Mark Krueger', 'Dylan Keats']),
    ('Saga GO', ['Samguk Han', 'Wanli Changcheng', 'Gabriel Garcia', 'Arion Sherwind', 'Riccardo Di Rigo', 'Adé Kébé',
                 'Victor Blade', 'Sol Daystar', 'Zanark Avalonic', 'Fei Rune']),
]


def fila(filas, nombre):
    todas = [d for d in filas if d['nombre'].lower().startswith(nombre.lower())]
    base = [d for d in todas if d['nombre'].strip().lower() == nombre.lower()]
    if not base:
        return None
    pos = collections.Counter(d['posicion'] for d in base).most_common(1)[0][0]
    elem = next((d['elemento'] for d in base if d['elemento']), '')
    celdas = []
    for j in JUEGOS:
        vals = []
        for d in base:
            if d['juego'] == j:
                t = '%s/%s/%s' % (d['ATT'], d['CTL'], d['DEF']) + ('' if d['posicion'] == pos else ' (%s)' % d['posicion'])
                if t not in vals:
                    vals.append(t)
        celdas.append(' · '.join(vals) or '—')
    especiales = []
    for d in todas:
        if d not in base:
            etiqueta = d['nombre'][len(nombre):].strip(' ()　') or d['nombre']
            etiqueta = etiqueta.replace('Adult', 'Adulto').replace('adulto', 'Adulto').replace('Adultoo', 'Adulto').replace('Adultoe', 'Adulto')
            t = '%s %s: %s/%s/%s' % (d['juego'], etiqueta, d['ATT'], d['CTL'], d['DEF'])
            if t not in especiales:
                especiales.append(t)
    return '| %s | %s | %s | %s | %s |' % (nombre, pos, ELEMENTOS.get(elem, elem), ' | '.join(celdas), ' · '.join(especiales) or '—')


def porcentaje(filas, pa, sa, pb, sb, rnd):
    a = [int(r[sa]) for r in filas if r['posicion'] == pa]
    b = [int(r[sb]) for r in filas if r['posicion'] == pb]
    return round(sum(rnd.choice(a) > rnd.choice(b) for _ in range(40000)) / 400)


def main():
    filas = list(csv.DictReader(open('data/stats/stats-por-juego.csv')))
    out = ['# Ejemplos de Cartas (fórmula v4, versión por juego)', '',
           'Calculadas con `formula-stats.md`. Formato: **ATT / CTL / DEF**. Cada valor es una carta distinta (juego y versión). '
           'Datos completos: `data/stats/stats-por-juego.csv`. Este archivo se genera con `scripts/ejemplos_cartas.py`.', '',
           '- Si la base tiene dos fichas del mismo personaje en un juego (p. ej. dos equipos en IE3), aparecen las dos.',
           '- GO1 no indica el elemento en la base de datos.', '']
    for titulo, nombres in GRUPOS:
        out += ['## ' + titulo, '', '| Personaje | Pos | Elemento | ' + ' | '.join(JUEGOS) + ' | Versiones especiales |',
                '|---|---|---|' + '---|' * len(JUEGOS) + '---|']
        out += [f for f in (fila(filas, n) for n in nombres) if f]
        out.append('')
    rnd = random.Random(3)
    out += ['## Balance de duelos', '', 'Cartas al azar de cada posición (todas las versiones de los 6 juegos):', '',
            '| Duelo | Gana el primero |', '|---|---|']
    for texto, args in [('Delantero (ATT) vs. defensa (DEF)', ('DL', 'ATT', 'DF', 'DEF')),
                        ('Delantero (ATT) vs. portero (DEF)', ('DL', 'ATT', 'PR', 'DEF')),
                        ('Medio (ATT) vs. defensa (DEF)', ('MC', 'ATT', 'DF', 'DEF')),
                        ('Medio (CTL) vs. delantero (CTL)', ('MC', 'CTL', 'DL', 'CTL')),
                        ('Portero (DEF) más alta que defensa (DEF)', ('PR', 'DEF', 'DF', 'DEF'))]:
        out.append('| %s | %d %% |' % (texto, porcentaje(filas, *args, rnd)))
    out += ['', '## Jugadores normales', '', 'Mínimo · flojo (p25) · normal (mediana) · bueno (p75) · máximo, con todas las versiones de los 6 juegos:', '',
            '| Posición | ATT | CTL | DEF |', '|---|---|---|---|']
    for p in ['PR', 'DF', 'MC', 'DL']:
        celdas = []
        for s in ['ATT', 'CTL', 'DEF']:
            v = sorted(int(r[s]) for r in filas if r['posicion'] == p)
            celdas.append(' · '.join(str(v[int(q * (len(v) - 1))]) for q in (0, .25, .5, .75, 1)))
        out.append('| %s | %s |' % (p, ' | '.join(celdas)))
    open('docs/ejemplos-cartas.md', 'w').write('\n'.join(out) + '\n')


if __name__ == '__main__':
    main()
