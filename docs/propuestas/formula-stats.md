# Propuesta: Fórmula de ATT / CTL / DEF

Estado: **propuesta, no aprobada**. Script: `scripts/stats_ds.py`. Resultado para las 2270 fichas de IE1–IE3: `data/propuestas/stats-ds.csv`.

## Pasos

### 1. Stat bruta a partir de las 7 stats de DS/3DS

Pesos basados en la tabla de acciones de IE2 (`referencias/stats-juegos-ds.md`) y en la definición de cada stat del GDD (2.2):

| Stat | Fórmula | Base |
|---|---|---|
| ATT (tiro) | 80 % Kick + 10 % Control + 10 % Guts | Tiro de IE2 |
| CTL (control, pase, regate, movilidad) | 50 % Body + 25 % Control + 25 % Speed | Regate de IE2 + "movilidad" del GDD |
| DEF (defensa) | 70 % Guard + 10 % Control + 10 % Stamina + 10 % Guts | Defensa con técnica de IE2 |
| DEF del portero (parada) | 80 % Guard + 10 % Body + 10 % Guts | Parada con técnica de IE2 |

### 2. Posición relativa frente a todos los jugadores

Se compara cada stat bruta con la de las 2270 fichas y se pasa a escala de carta:

`carta = 50 + 49 × percentil^1,3`

- El mejor de todos llega a 99 y el peor queda en 50.
- El exponente 1,3 reserva los números altos para los mejores.

### 3. Factor por posición

La stat principal de cada posición se queda igual y las secundarias se reducen:

| Posición | ATT | CTL | DEF |
|---|---|---|---|
| PR | ×0,55 | ×0,8 | ×1 |
| DF | ×0,8 | ×0,9 | ×1 |
| MC | ×0,9 | ×1 | ×0,85 |
| DL | ×1 | ×0,9 | ×0,6 |

## Ejemplos

| Jugador | Juego | Pos | ATT | CTL | DEF |
|---|---|---|---|---|---|
| Mark Evans | IE1 | PR | 52 | 77 | 98 |
| Axel Blaze | IE1 | DL | 98 | 86 | 51 |
| Jude Sharp | IE1 | MC | 77 | 99 | 84 |
| Kevin Dragonfly | IE1 | DL | 93 | 67 | 47 |
| Bobby Shearer | IE1 | DF | 78 | 77 | 97 |
| Nathan Swift | IE1 | DF | 67 | 80 | 62 |
| Jack Wallside | IE1 | DF | 62 | 73 | 80 |
| Tod Ironside | IE1 | DF | 52 | 54 | 64 |
| William Glass | IE1 | DL | 69 | 56 | 40 |
| Byron Love | IE2 | MC | 88 | 97 | 79 |
| Xavier Foster | IE3 | DL | 92 | 81 | 41 |
| Shawn Froste | IE3 | DL | 79 | 83 | 44 |
| Darren LaChance | IE3 | PR | 42 | 53 | 92 |

## Limitaciones

- Las stats de nivel 99 de los juegos a veces no reflejan la fama del personaje. Ej.: Shawn Froste en IE3 tiene Kick 61, así que su ATT sale bajo. Estos casos se ajustarían a mano o eligiendo la versión de otro juego.
- Solo cubre IE1–IE3. Para GO, Ares y Victory Road haría falta otra fuente (p. ej. las stats de Victory Road) o ponerlas a mano.
- Los factores por posición y el rango 50–99 son ajustables.
