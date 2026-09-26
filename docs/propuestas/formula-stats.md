# Propuesta: Fórmula de ATT / CTL / DEF (v2)

Estado: **propuesta, no aprobada**. Script: `scripts/stats_cartas.py`. Resultados:
- `data/propuestas/stats-ds.csv`: 2270 fichas de IE1–IE3 (stats de nivel 99).
- `data/propuestas/stats-strikers.csv`: fichas de GO Strikers 2013 Xtreme (IEGSX), con varias versiones por personaje según su época o equipo.

La v1 salía demasiado alta (99) y daba ATT alto a los porteros. Esta versión se calibra con las cartas oro top de Madfut (`referencias/madfut-pacybits.md`, apartado "Calibración").

## Pasos

### 1. Stat bruta

| Stat | DS/3DS (IE1–IE3) | Strikers (IEGSX) |
|---|---|---|
| ATT | 80 % Kick + 10 % Control + 10 % Guts | 80 % Kick + 20 % Control |
| CTL | 50 % Body + 25 % Control + 25 % Speed | 50 % Body + 25 % Control + 25 % Speed |
| DEF | 70 % Guard + 10 % Control + 10 % Stamina + 10 % Guts | Guard |
| DEF del portero | 80 % Guard + 10 % Body + 10 % Guts | 80 % Catch + 20 % Guard |

### 2. Comparación solo con los de su posición

Cada stat se compara únicamente con jugadores de la misma posición (porteros con porteros, delanteros con delanteros…). Por eso el ATT de un portero siempre sale bajo aunque tenga buen Kick.

### 3. Rango de cada posición

`carta = mínimo + (máximo − mínimo) × percentil^1,3`

| Posición | ATT | CTL | DEF |
|---|---|---|---|
| PR | 20 – 45 | 20 – 45 | 50 – 89 |
| DF | 30 – 70 | 35 – 75 | 50 – 89 |
| MC | 45 – 86 | 50 – 89 | 35 – 80 |
| DL | 50 – 89 | 45 – 88 | 20 – 62 |

- Los techos son los de las cartas oro top de Madfut (stat principal 86–89).
- Por encima de 89 quedan solo las cartas Especiales.
- El exponente 1,3 hace que la mayoría queden en la zona media y solo los mejores lleguen arriba.

## Ejemplos (datos de DS/3DS)

| Jugador | Juego | Pos | ATT | CTL | DEF |
|---|---|---|---|---|---|
| Mark Evans | IE1 | PR | 43 | 45 | 87 |
| Axel Blaze | IE1 | DL | 88 | 85 | 53 |
| Jude Sharp | IE1 | MC | 77 | 89 | 80 |
| Byron Love | IE2 | MC | 85 | 87 | 77 |
| Bobby Shearer | IE1 | DF | 70 | 66 | 88 |
| Kevin Dragonfly | IE1 | DL | 82 | 64 | 46 |
| Xavier Foster | IE3 | DL | 81 | 79 | 36 |
| Jack Wallside | IE1 | DF | 54 | 62 | 72 |
| William Glass | IE1 | DL | 62 | 55 | 35 |
| Tod Ironside | IE1 | DF | 44 | 45 | 61 |

Comparación con Madfut: Mbappé 89/83/42, De Bruyne 86/89/64, Van Dijk 67/70/87, Alisson 41/43/88.

## Ejemplos (datos de Strikers)

Strikers tiene stats en saltos de 10 (50–110) y **varias versiones por personaje según su época** (Raimon 1, Inazuma Japón, ILJ…). Encaja con las cartas por era del GDD: las versiones tempranas salen más bajas y las tardías más altas.

| Carta | Pos | ATT | CTL | DEF |
|---|---|---|---|---|
| Axel Blaze (Raimon 1) | DL | 53 | 51 | 28 |
| Axel Blaze (Inazuma Japón) | DL | 69 | 70 | 46 |
| Jude Sharp (Raimon 1) | MC | 48 | 55 | 35 |
| Jude Sharp (Inazuma Japón) | MC | 81 | 78 | 38 |
| Mark Evans (Raimon 1) | PR | 23 | 21 | 82 |
| Arion Sherwind | MC | 81 | 78 | 72 |
| Victor Blade | DL | 81 | 70 | 46 |

## Limitaciones

- Las stats de los juegos no siempre reflejan la fama del personaje (ej. Shawn Froste en IE3 tiene Kick 61). Se ajustaría a mano o eligiendo otra versión.
- Los saltos de 10 de Strikers producen muchos empates.
- Rangos y curva ajustables.
