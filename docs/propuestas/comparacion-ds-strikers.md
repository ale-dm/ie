# Comparación: Stats con Datos de DS vs. Strikers (fórmula v3)

Misma fórmula v3 (`formula-stats.md`, escala proporcional) aplicada a las dos fuentes. Tabla completa de los 102 personajes que salen en ambas, con la mejor versión de cada fuente: `data/propuestas/comparacion-ds-strikers.csv`.

## Personajes principales (ATT/CTL/DEF)

| Personaje | DS | Strikers (por versión) |
|---|---|---|
| Mark Evans | IE1 38/42/75 · IE3 29/31/76 | Raimon 1 35/37/86 · Raimon 2 42/39/73 · Inazuma Japón 41/41/81 · ILJ 43/45/87 |
| Axel Blaze | IE1 76/75/49 · IE3 74/69/44 | Raimon 1 71/70/43 · Raimon 2 80/73/43 · Inazuma Japón 79/78/49 · ILJ 89/85/49 |
| Jude Sharp | IE1 66/78/68 · IE3 66/66/50 | Raimon 1 62/72/36 · Raimon 2 69/76/44 · Inazuma Japón 77/83/50 · ILJ 85/89/64 |
| Kevin Dragonfly | IE1 69/64/47 · IE2 89/76/57 | Raimon 1 73/63/36 · Inazuma Japón 79/73/55 · ILJ 88/82/49 |
| Bobby Shearer | IE1 60/59/73 | Raimon 1 50/54/72 · Raimon 2 57/56/72 · Selección Mundial 59/62/80 |
| Jack Wallside | IE1 49/58/62 · IE3 35/51/63 | Raimon 1 57/48/81 · Inazuma Japón 64/56/80 · ILJ 60/59/87 |
| Byron Love | IE2 79/72/62 | Zeus 82/74/50 · Selección Mundial 77/76/57 · Adulto 86/86/64 |
| Shawn Froste | IE3 61/72/45 | Raimon 2 57/58/73 · Inazuma Japón 79/75/62 · ILJ 89/81/62 |
| Tod Ironside | IE1 44/52/55 | Raimon 1 56/61/62 · Inazuma Japón 59/66/64 · Emperadores Oscuros 68/74/57 |

## Coincidencia entre fuentes (100 personajes en la misma posición, mejor versión)

| Stat | Correlación | Diferencia media | Diferencia de 10 o más |
|---|---|---|---|
| ATT | 0,75 | 8 puntos | 37 % |
| CTL | 0,77 | 7 puntos | 29 % |
| DEF | 0,69 | 8 puntos | 34 % |

Con la v2 (percentil) la diferencia media era de 12–16 puntos: buena parte venía del error de la fórmula, no de los datos.

## Pros y contras

| | DS (IE1–IE3) | Strikers (IEGSX) |
|---|---|---|
| Personajes | ~1850 distintos, solo IE1–IE3, muchos genéricos | ~310 distintos, IE1–IE3 **y GO/Chrono Stone/Galaxy** |
| Versiones por época | Una por juego; entre juegos no siempre suben | **Varias por personaje, subiendo en saltos de ~10 %** |
| Precisión | Stats de 1 en 1 | Saltos de 10 (+2 del Key bonus): más empates |
| Valores | Más repartidos (mediana ATT de DL: 59) | Más altos y juntos (mediana ATT de DL: 79) |
| Incoherencias | IE3 a nivel 99 baja a algunas estrellas | Algunas del juego (Mark Raimon 2 con Catch 90) |
