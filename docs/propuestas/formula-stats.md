# Propuesta: Fórmula de ATT / CTL / DEF (v3)

Estado: **propuesta, no aprobada**. Script: `scripts/stats_cartas.py`. Resultados:
- `data/propuestas/stats-ds.csv`: 2270 fichas de IE1–IE3 (stats de nivel 99).
- `data/propuestas/stats-strikers.csv`: fichas de GO Strikers 2013 Xtreme, con varias versiones por personaje.

## Historial

- **v1:** escala 50–99 frente a todos los jugadores. Demasiado alta, y los porteros salían con ATT alto.
- **v2:** percentil dentro de cada posición. **Error:** el percentil mide el puesto, no la diferencia real. Con las stats de Strikers en saltos de 10, subir 10 puntos adelantaba a muchos jugadores de golpe y exageraba las diferencias entre versiones (Axel Raimon 1 salía con 53 de ATT e ILJ con 89). Además no se sumaba el Key bonus de Strikers.
- **v3 (esta):** escala **proporcional**. Si en el juego un jugador tiene un 10 % más, en la carta también tiene un 10 % más. Se suma el Key bonus.

## Pasos

### 1. Stat bruta

| Stat | DS/3DS (IE1–IE3) | Strikers (IEGSX) |
|---|---|---|
| ATT | 80 % Kick + 10 % Control + 10 % Guts | 80 % Kick + 20 % Control |
| CTL | 50 % Body + 25 % Control + 25 % Speed | 50 % Body + 25 % Control + 25 % Speed |
| DEF | 70 % Guard + 10 % Control + 10 % Stamina + 10 % Guts | Guard |
| DEF del portero | 80 % Guard + 10 % Body + 10 % Guts | 80 % Catch + 20 % Guard |

En Strikers se suma antes el **Key bonus** de cada ficha (+2 a dos stats, ej. "Kick +2/Guard +2").

### 2. Escala proporcional por posición

`carta = techo de la posición × stat bruta / mejor stat bruta de esa posición`

| Posición | Techo ATT | Techo CTL | Techo DEF |
|---|---|---|---|
| PR | 45 | 45 | 89 |
| DF | 70 | 75 | 89 |
| MC | 86 | 89 | 80 |
| DL | 89 | 88 | 62 |

- Los techos son los de las cartas oro top de Madfut. Por encima de 89 quedan las cartas Especiales.
- Cada stat se compara solo con los de su posición, así que un portero nunca tiene ATT alto.

## Ejemplos con Strikers (versiones de un mismo personaje)

Entre corchetes, las stats originales del juego (Kick / Body / Control / Guard / Catch, ya con el Key bonus).

| Carta | ATT | CTL | DEF | Stats del juego |
|---|---|---|---|---|
| Axel Blaze (Raimon 1) | 71 | 70 | 43 | K92 B92 C80 G70 |
| Axel Blaze (Raimon 2) | 80 | 73 | 43 | K102 B90 C92 G70 |
| Axel Blaze (Inazuma Japón) | 79 | 78 | 49 | K102 B100 C90 G80 |
| Axel Blaze (ILJ, adulto) | 89 | 85 | 49 | K112 B100 C110 G80 |
| Jude Sharp (Raimon 1) | 62 | 72 | 36 | K70 B80 C94 G50 |
| Jude Sharp (Inazuma Japón) | 77 | 83 | 50 | K90 B102 C102 G70 |
| Jude Sharp (ILJ) | 85 | 89 | 64 | K100 B110 C112 G90 |
| Mark Evans (Raimon 1) | 35 | 37 | 86 | Catch 110, Guard 92 |
| Mark Evans (Raimon 2) | 42 | 39 | 73 | Catch 90, Guard 92 |
| Mark Evans (Inazuma Japón) | 41 | 41 | 81 | Catch 100, Guard 102 |
| Mark Evans (ILJ) | 43 | 45 | 87 | Catch 110, Guard 102 |

Las diferencias que quedan entre versiones son las del propio juego: el Kick de Axel es 92 → 102 → 112. Lo de Mark Raimon 2 viene de que el juego le baja la Catch de 110 a 90.

## Ejemplos con DS

| Jugador | Juego | Pos | ATT | CTL | DEF |
|---|---|---|---|---|---|
| Mark Evans | IE1 | PR | 38 | 42 | 75 |
| Axel Blaze | IE1 | DL | 76 | 75 | 49 |
| Jude Sharp | IE1 | MC | 66 | 78 | 68 |
| Kevin Dragonfly | IE2 | DL | 89 | 76 | 57 |
| Byron Love | IE2 | MC | 79 | 72 | 62 |
| Bobby Shearer | IE1 | DF | 60 | 59 | 73 |
| Tod Ironside | IE1 | DF | 44 | 52 | 55 |

## Diferencia entre fuentes

- **DS** incluye muchos jugadores genéricos flojos, así que sus valores bajan más: la mediana de ATT de un DL es 59.
- **Strikers** solo tiene personajes conocidos, así que sus valores quedan más altos y juntos: la mediana de ATT de un DL es 79.
