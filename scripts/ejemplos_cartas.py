"""Genera docs/ejemplos-cartas.md a partir de data/cartas/cartas.csv (cartas ya cribadas). Uso: python3 scripts/ejemplos_cartas.py"""
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


def fila(cartas, nombre):
    """Una fila por personaje con todas sus cartas: versión y ATT/CTL/DEF."""
    import re
    base = re.sub(r'\s+', ' ', nombre).lower()
    propias = [c for c in cartas if re.sub(r'\s*\(.*?\)', '', c['nombre']).strip().lower().replace('-', ' ') == base.replace('-', ' ')]
    if not propias:
        return None
    pos = collections.Counter(c['posicion'] for c in propias).most_common(1)[0][0]
    elem = next((c['elemento'] for c in propias if c['elemento']), '')
    lista = ' · '.join('%s (%s): %s/%s/%s%s' % (c['version'], c['juego'], c['ATT'], c['CTL'], c['DEF'],
                                               '' if c['posicion'] == pos else ' [%s]' % c['posicion']) if c['version'] != c['juego']
                       else '%s: %s/%s/%s%s' % (c['juego'], c['ATT'], c['CTL'], c['DEF'], '' if c['posicion'] == pos else ' [%s]' % c['posicion'])
                       for c in propias)
    return '| %s | %s | %s | %s |' % (nombre, pos, ELEMENTOS.get(elem, elem), lista)


def porcentaje(filas, pa, sa, pb, sb, rnd):
    a = [int(r[sa]) for r in filas if r['posicion'] == pa]
    b = [int(r[sb]) for r in filas if r['posicion'] == pb]
    return round(sum(rnd.choice(a) > rnd.choice(b) for _ in range(40000)) / 400)


def main():
    filas = list(csv.DictReader(open('data/cartas/cartas.csv')))
    out = ['# Ejemplos de Cartas', '',
           'Cartas ya cribadas (`data/cartas/cartas.csv`, reglas en GDD 2.2) con stats de `formula-stats.md`. Formato: **versión (juego): ATT / CTL / DEF**. '
           'Este archivo se genera con `scripts/ejemplos_cartas.py`.', '',
           '- GO1 no indica el elemento en la base de datos.', '']
    for titulo, nombres in GRUPOS:
        out += ['## ' + titulo, '', '| Personaje | Pos | Elemento | Cartas |', '|---|---|---|---|']
        out += [f for f in (fila(filas, n) for n in nombres) if f]
        out.append('')
    rnd = random.Random(3)
    out += ['## Balance de duelos', '', 'Cartas al azar de cada posición (todas las cartas cribadas):', '',
            '| Duelo | Gana el primero |', '|---|---|']
    for texto, args in [('Delantero (ATT) vs. defensa (DEF)', ('DL', 'ATT', 'DF', 'DEF')),
                        ('Delantero (ATT) vs. portero (DEF)', ('DL', 'ATT', 'PR', 'DEF')),
                        ('Medio (ATT) vs. defensa (DEF)', ('MC', 'ATT', 'DF', 'DEF')),
                        ('Medio (CTL) vs. delantero (CTL)', ('MC', 'CTL', 'DL', 'CTL')),
                        ('Portero (DEF) más alta que defensa (DEF)', ('PR', 'DEF', 'DF', 'DEF'))]:
        out.append('| %s | %d %% |' % (texto, porcentaje(filas, *args, rnd)))
    out += ['', '## Jugadores normales', '', 'Mínimo · flojo (p25) · normal (mediana) · bueno (p75) · máximo, con todas las cartas cribadas:', '',
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
